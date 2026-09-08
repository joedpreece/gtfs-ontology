import re
from pathlib import Path
from typing import List, Tuple

import markdown
import pandas as pd
from markdown_it import MarkdownIt

md_text = Path("/home/joe/Projects/research/transit/gtfs-ontology/scripts/reference.md").read_text(encoding="utf-8")

md = MarkdownIt("commonmark")
tokens = md.parse(md_text)

html = markdown.markdown(md_text, extensions=["tables"])

tables = pd.read_html(html)

def filename_to_class(filename: str) -> str:
    # remove extension
    name = re.sub(r"\.(txt|geojson)$", "", filename)

    # singularize naively
    words = []
    for part in name.split("_"):
        if part.endswith("ies"):
            part = part[:-3] + "y"
        elif part.endswith("s"):
            part = part[:-1]

        words.append(part.capitalize())

    return "".join(words)

def rename(table: pd.DataFrame) -> List[Tuple[str, str, str, str]]:
    table = table.dropna()

    fields = []
    for index, row in table.iterrows():
        name = row["Field Name"]
        field_type = row["Type"]
        presence = row["Presence"]
        description = row["Description"]

        fields.append((name, field_type, presence, description))
    return fields

def rename2(
        fields: List[Tuple[str, str, str, str]],
        class_name: str
):
    for name, field_type, presence, description in fields:


        if name == "parent_station":
            prop = types.new_class("hasParentStation", (DataProperty,))
            prop.domain = [onto[class_name]]
            prop.comment = [description]

        else:

            prop = types.new_class(name, (DataProperty,))

            prop.domain = [onto[class_name]]
            prop.comment = [description]


from owlready2 import *

onto = get_ontology("http://example.org/gtfs")

class_names = []
for index, row in tables[0].iterrows():
    name = filename_to_class(row["File Name"])
    description = row["Description"]
    class_names.append((name, description))

print(tables[3])

agency_fields = rename(tables[1])
stop_fields = rename(tables[2])
route_fields = rename(tables[3])
trip_fields = rename(tables[4])
stop_time_fields = rename(tables[6])
calendar_fields = rename(tables[7])
calendar_date_fields = rename(tables[8])

# fare_media_fields = rename(tables[8])
# fare_product_fields = rename(tables[9])
# rider_category_fields = rename(tables[10])
# fare1_leg_rule_fields = rename(tables[11])

with onto:

    # Create the classes
    for name, description in class_names:
        cls = types.new_class(name, (Thing,))
        cls.comment = [description]

        object_prop = types.new_class(f"has{name}", (ObjectProperty,))
        object_prop.range = [cls]

        inverse_prop = types.new_class(f"is{name}Of", (ObjectProperty,))
        inverse_prop.domain = [cls]

        object_prop.inverse_property = inverse_prop

    rename2(agency_fields, "Agency")
    rename2(stop_fields, "Stop")
    rename2(route_fields, "Route")
    rename2(trip_fields, "Trip")
    rename2(stop_time_fields, "StopTime")
    rename2(calendar_fields, "Calendar")
    rename2(calendar_date_fields, "CalendarDate")

onto.save("gtfs_parse_test.rdf")