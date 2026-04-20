from gtfs_ontology.schedule import *

with gtfs:

    rules = Imp()

    rules.set_as_rule("""
Agency(?a),


"""
    )