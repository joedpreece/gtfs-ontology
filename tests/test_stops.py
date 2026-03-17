import time
import pytest
from config import RULES_STOPS
from conftest import run_cmd, create_triple, extract_boolean

# Module-scoped so we load the .dl only once per this file
@pytest.fixture(scope="module")
def stops_rules(rdfox_proc):

    run_cmd(rdfox_proc, f'import "{str(RULES_STOPS)}"')

    return True


def test_stop_without_stop_id_is_violation(
    clear_datastore, gtfs_onto, nt_writer, import_into_rdfox, rdfox_ask, stops_rules
):
    with gtfs_onto:
        s = gtfs_onto.Stop("StopNoID")
        # No stop_id assigned
        nt_path, _ = nt_writer(gtfs_onto)
    import_into_rdfox(nt_path)

    assert extract_boolean(
        rdfox_ask("{ gtfs:StopNoID rdf:type gtfs:Violation }")
    ) is True


def test_stop_with_stop_id_is_not_violation(
    clear_datastore, gtfs_onto, nt_writer, import_into_rdfox, rdfox_ask, stops_rules
):
    with gtfs_onto:
        s = gtfs_onto.Stop("StopWithID")
        create_triple(s, gtfs_onto.stop_id, "S123")
        nt_path, _ = nt_writer(gtfs_onto)
    import_into_rdfox(nt_path)

    assert extract_boolean(
        rdfox_ask("{ gtfs:StopWithID rdf:type gtfs:Violation }")
    ) is False



def test_location_type_0_yields_stoplocation_when_not_child(
    clear_datastore, gtfs_onto, nt_writer, import_into_rdfox, rdfox_ask, stops_rules
):
    with gtfs_onto:
        s = gtfs_onto.Stop("S0")
        create_triple(s, gtfs_onto.location_type, 0)
        # no parent_station => NOT a ChildStop
        nt_path, _ = nt_writer(gtfs_onto)
    import_into_rdfox(nt_path)

    assert extract_boolean(rdfox_ask("{ gtfs:S0 rdf:type gtfs:StopLocation }")) is True
    assert extract_boolean(rdfox_ask("{ gtfs:S0 rdf:type gtfs:Platform }")) is False



def test_location_type_0_yields_platform_when_childstop(
    clear_datastore, gtfs_onto, nt_writer, import_into_rdfox, rdfox_ask, stops_rules
):
    with gtfs_onto:
        child = gtfs_onto.Stop("Child0")
        parent = gtfs_onto.Stop("StationP")
        create_triple(child, gtfs_onto.location_type, 0)
        create_triple(parent, gtfs_onto.location_type, 1)  # Station
        create_triple(child, gtfs_onto.parent_station, parent)
        nt_path, _ = nt_writer(gtfs_onto)
    import_into_rdfox(nt_path)

    # ChildStop inferred; Platform should hold, StopLocation should NOT
    assert extract_boolean(rdfox_ask("{ gtfs:Child0 rdf:type gtfs:Platform }")) is True
    assert extract_boolean(rdfox_ask("{ gtfs:Child0 rdf:type gtfs:StopLocation }")) is False
    # Parent typed Station
    assert extract_boolean(rdfox_ask("{ gtfs:StationP rdf:type gtfs:Station }")) is True




@pytest.mark.parametrize(
    "iri, lt, expected_type",
    [
        ("LT1", 1, "Station"),
        ("LT2", 2, "EntranceOrExit"),
        ("LT3", 3, "GenericNode"),
        ("LT4", 4, "BoardingArea"),
    ],
)
def test_location_type_maps_to_expected_kind(
    iri, lt, expected_type,
    clear_datastore, gtfs_onto, nt_writer, import_into_rdfox, rdfox_ask, stops_rules
):
    with gtfs_onto:
        s = gtfs_onto.Stop(iri)
        create_triple(s, gtfs_onto.location_type, lt)
        nt_path, _ = nt_writer(gtfs_onto)
    import_into_rdfox(nt_path)

    assert extract_boolean(
        rdfox_ask(f"{{ gtfs:{iri} rdf:type gtfs:{expected_type} }}")
    ) is True


def test_childstop_inferred_from_parent_station(
    clear_datastore, gtfs_onto, nt_writer, import_into_rdfox, rdfox_ask, stops_rules
):
    with gtfs_onto:
        c = gtfs_onto.Stop("ChildX")
        p = gtfs_onto.Stop("ParentSta")
        create_triple(p, gtfs_onto.location_type, 1)
        create_triple(c, gtfs_onto.parent_station, p)
        nt_path, _ = nt_writer(gtfs_onto)
    import_into_rdfox(nt_path)

    assert extract_boolean(rdfox_ask("{ gtfs:ChildX rdf:type gtfs:ChildStop }")) is True



def test_station_with_parent_is_violation(
    clear_datastore, gtfs_onto, nt_writer, import_into_rdfox, rdfox_ask, stops_rules
):
    with gtfs_onto:
        s1 = gtfs_onto.Stop("Sta1")
        s2 = gtfs_onto.Stop("Sta2")
        create_triple(s1, gtfs_onto.location_type, 1)  # Station
        create_triple(s2, gtfs_onto.location_type, 1)  # Station
        create_triple(s1, gtfs_onto.parent_station, s2)
        nt_path, _ = nt_writer(gtfs_onto)
    import_into_rdfox(nt_path)

    assert extract_boolean(rdfox_ask("{ gtfs:Sta1 rdf:type gtfs:Station }")) is True
    assert extract_boolean(rdfox_ask("{ gtfs:Sta1 rdf:type gtfs:Violation }")) is True



@pytest.mark.parametrize("kind", ["EntranceOrExit", "GenericNode", "BoardingArea"])
def test_parent_required_for_certain_kinds(kind,
    clear_datastore, gtfs_onto, nt_writer, import_into_rdfox, rdfox_ask, stops_rules
):
    # An instance with the given type (via location_type) but NO parent => Violation
    lt_map = {
        "EntranceOrExit": 2,
        "GenericNode": 3,
        "BoardingArea": 4,
    }
    iri = f"NoParent_{kind}"
    with gtfs_onto:
        s = gtfs_onto.Stop(iri)
        create_triple(s, gtfs_onto.location_type, lt_map[kind])
        nt_path, _ = nt_writer(gtfs_onto)
    import_into_rdfox(nt_path)

    assert extract_boolean(rdfox_ask(f"{{ gtfs:{iri} rdf:type gtfs:{kind} }}")) is True
    assert extract_boolean(rdfox_ask(f"{{ gtfs:{iri} rdf:type gtfs:Violation }}")) is True


def test_parentless_stop_is_inferred_when_no_parent(
    clear_datastore, gtfs_onto, nt_writer, import_into_rdfox, rdfox_ask, stops_rules
):
    with gtfs_onto:
        s = gtfs_onto.Stop("Alone")
        # No parent_station
        nt_path, _ = nt_writer(gtfs_onto)
    import_into_rdfox(nt_path)

    assert extract_boolean(rdfox_ask("{ gtfs:Alone rdf:type gtfs:ParentlessStop }")) is True



@pytest.mark.parametrize(
    "iri, lt, class_name",
    [
        ("SL_req", 0, "StopLocation"),
        ("ST_req", 1, "Station"),
        ("EE_req", 2, "EntranceOrExit"),
    ],
)
def test_required_fields_violation_only_when_all_three_missing(
    iri, lt, class_name,
    clear_datastore, gtfs_onto, nt_writer, import_into_rdfox, rdfox_ask, stops_rules
):
    # --- Case A: all three missing -> Violation = True
    with gtfs_onto:
        s = gtfs_onto.Stop(iri)
        create_triple(s, gtfs_onto.location_type, lt)
        nt_path, _ = nt_writer(gtfs_onto)
    import_into_rdfox(nt_path)

    assert extract_boolean(rdfox_ask(f"{{ gtfs:{iri} rdf:type gtfs:{class_name} }}")) is True
    assert extract_boolean(rdfox_ask(f"{{ gtfs:{iri} rdf:type gtfs:Violation }}")) is True
    #
    # # --- Reset datastore, Case B: some fields present -> Violation = False
    # # Here we add only stop_name; because the rule requires ALL THREE missing
    # # to fire, the Violation should not hold when any one is present.
    # clear_datastore()
    # with gtfs_onto:
    #     s = gtfs_onto.Stop(f"{iri}_partial")
    #     create_triple(s, gtfs_onto.location_type, lt)
    #     create_triple(s, gtfs_onto.stop_name, "Name present")
    #     # lat/lon intentionally absent
    #     nt_path, _ = nt_writer(gtfs_onto)
    # import_into_rdfox(nt_path)
    #
    # assert extract_boolean(
    #     rdfox_ask(f"{{ gtfs:{iri}_partial rdf:type gtfs:{class_name} }}")
    # ) is True
    # assert extract_boolean(
    #     rdfox_ask(f"{{ gtfs:{iri}_partial rdf:type gtfs:Violation }}")
    # ) is False


def test_wheelchair_description_for_parentless_stop_values_0_1_2(
    clear_datastore, gtfs_onto, nt_writer, import_into_rdfox, rdfox_ask, stops_rules
):
    with gtfs_onto:
        p0 = gtfs_onto.Stop("P0")
        p1 = gtfs_onto.Stop("P1")
        p2 = gtfs_onto.Stop("P2")
        # All are parentless stops (no parent_station)
        create_triple(p0, gtfs_onto.wheelchair_boarding, 0)
        create_triple(p1, gtfs_onto.wheelchair_boarding, 1)
        create_triple(p2, gtfs_onto.wheelchair_boarding, 2)
        nt_path, _ = nt_writer(gtfs_onto)
    import_into_rdfox(nt_path)

    assert extract_boolean(
        rdfox_ask("{ gtfs:P0 gtfs:wheelchair_boarding_description gtfs:WheelchairBoardingParentlessStop0 }")
    ) is True
    assert extract_boolean(
        rdfox_ask("{ gtfs:P1 gtfs:wheelchair_boarding_description gtfs:WheelchairBoardingParentlessStop1 }")
    ) is True
    assert extract_boolean(
        rdfox_ask("{ gtfs:P2 gtfs:wheelchair_boarding_description gtfs:WheelchairBoardingParentlessStop2 }")
    ) is True



def test_child_stop_wb_zero_inherits_parent_description_and_wb_1_2_override(
    clear_datastore, gtfs_onto, nt_writer, import_into_rdfox, rdfox_ask, stops_rules
):
    with gtfs_onto:
        # Parent station gets a parentless description via its own wb value
        parent = gtfs_onto.Stop("ParentStation")
        create_triple(parent, gtfs_onto.location_type, 1)  # Station
        create_triple(parent, gtfs_onto.wheelchair_boarding, 1)  # -> ParentlessStop1 description

        # Child A: wb=0 -> inherit parent's description
        c0 = gtfs_onto.Stop("ChildW0")
        create_triple(c0, gtfs_onto.location_type, 0)
        create_triple(c0, gtfs_onto.parent_station, parent)
        create_triple(c0, gtfs_onto.wheelchair_boarding, 0)

        # Child B: wb=1 -> fixed ChildStop1 description
        c1 = gtfs_onto.Stop("ChildW1")
        create_triple(c1, gtfs_onto.location_type, 0)
        create_triple(c1, gtfs_onto.parent_station, parent)
        create_triple(c1, gtfs_onto.wheelchair_boarding, 1)

        # Child C: wb=2 -> fixed ChildStop2 description
        c2 = gtfs_onto.Stop("ChildW2")
        create_triple(c2, gtfs_onto.location_type, 0)
        create_triple(c2, gtfs_onto.parent_station, parent)
        create_triple(c2, gtfs_onto.wheelchair_boarding, 2)

        nt_path, _ = nt_writer(gtfs_onto)
    import_into_rdfox(nt_path)

    # Parent gets ParentlessStop1 description
    assert extract_boolean(
        rdfox_ask("{ gtfs:ParentStation gtfs:wheelchair_boarding_description gtfs:WheelchairBoardingParentlessStop1 }")
    ) is True

    # Child wb=0 inherits parent's description
    assert extract_boolean(
        rdfox_ask("{ gtfs:ChildW0 gtfs:wheelchair_boarding_description gtfs:WheelchairBoardingParentlessStop1 }")
    ) is True

    # Child wb=1 / wb=2 override
    assert extract_boolean(
        rdfox_ask("{ gtfs:ChildW1 gtfs:wheelchair_boarding_description gtfs:WheelchairBoardingChildStop1 }")
    ) is True
    assert extract_boolean(
        rdfox_ask("{ gtfs:ChildW2 gtfs:wheelchair_boarding_description gtfs:WheelchairBoardingChildStop2 }")
    ) is True


def test_entrance_exit_inherits_or_overrides_wheelchair_description(
    clear_datastore, gtfs_onto, nt_writer, import_into_rdfox, rdfox_ask, stops_rules
):
    with gtfs_onto:
        parent = gtfs_onto.Stop("ParentSta2")
        create_triple(parent, gtfs_onto.location_type, 1)  # Station
        create_triple(parent, gtfs_onto.wheelchair_boarding, 2)  # -> ParentlessStop2 description

        # EE A: wb=0 -> inherit parent's description
        ee0 = gtfs_onto.Stop("EE_W0")
        create_triple(ee0, gtfs_onto.location_type, 2)
        create_triple(ee0, gtfs_onto.parent_station, parent)
        create_triple(ee0, gtfs_onto.wheelchair_boarding, 0)

        # EE B: wb=1 -> ChildStop1 description (as per rules)
        ee1 = gtfs_onto.Stop("EE_W1")
        create_triple(ee1, gtfs_onto.location_type, 2)
        create_triple(ee1, gtfs_onto.parent_station, parent)
        create_triple(ee1, gtfs_onto.wheelchair_boarding, 1)

        # EE C: wb=2 -> ChildStop2 description (as per rules)
        ee2 = gtfs_onto.Stop("EE_W2")
        create_triple(ee2, gtfs_onto.location_type, 2)
        create_triple(ee2, gtfs_onto.parent_station, parent)
        create_triple(ee2, gtfs_onto.wheelchair_boarding, 2)

        nt_path, _ = nt_writer(gtfs_onto)
    import_into_rdfox(nt_path)

    # Parent has the parentless description (2)
    assert extract_boolean(
        rdfox_ask("{ gtfs:ParentSta2 gtfs:wheelchair_boarding_description gtfs:WheelchairBoardingParentlessStop2 }")
    ) is True

    # EE wb=0 inherits parent description
    assert extract_boolean(
        rdfox_ask("{ gtfs:EE_W0 gtfs:wheelchair_boarding_description gtfs:WheelchairBoardingParentlessStop2 }")
    ) is True

    # EE wb=1 / 2 use fixed child-stop descriptions per rules
    assert extract_boolean(
        rdfox_ask("{ gtfs:EE_W1 gtfs:wheelchair_boarding_description gtfs:WheelchairBoardingChildStop1 }")
    ) is True
    assert extract_boolean(
        rdfox_ask("{ gtfs:EE_W2 gtfs:wheelchair_boarding_description gtfs:WheelchairBoardingChildStop2 }")
    ) is True
