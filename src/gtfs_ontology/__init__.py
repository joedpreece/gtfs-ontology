from pathlib import Path

from rdflib import Namespace
# from owlready2 import *

# Root directory of the project
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Sub directories
ARTEFACTS_DIR = PROJECT_ROOT / "artefacts"
GRAPHS_DIR = PROJECT_ROOT / "artefacts" / "graphs"
SHAPES_DIR = PROJECT_ROOT / "artefacts" / "shapes"
ONTOLOGIES_DIR = PROJECT_ROOT / "artefacts" / "ontologies"
MAPPINGS_DIR = PROJECT_ROOT / "artefacts" / "mappings"
DATA_DIR = PROJECT_ROOT / "data"

# Make directories if they don't exist
GRAPHS_DIR.mkdir(parents=True, exist_ok=True)
ONTOLOGIES_DIR.mkdir(parents=True, exist_ok=True)
SHAPES_DIR.mkdir(parents=True, exist_ok=True)
MAPPINGS_DIR.mkdir(parents=True, exist_ok=True)

# String IRIs
gtfs_rml_iri = "https://transit.ac.uk/mappings/gtfs"
gtfs_kg_iri = "https://transit.ac.uk/graphs/gtfs"
gtfs_owl_iri = "https://transit.ac.uk/ontologies/gtfs"
gtfs_shacl_iri = "https://transit.ac.uk/shapes/gtfs"

# Files
ONTOLOGY_FILE = ONTOLOGIES_DIR / "gtfs.owl.ttl"

AGENCY_FILE = DATA_DIR / "agency.txt"
AGENCY_RML_FILE = MAPPINGS_DIR / "agency.rml.ttl"
AGENCY_KG_FILE = GRAPHS_DIR / "agency.nt"

STOP_FILE = DATA_DIR / "stops.txt"
STOP_RML_FILE = MAPPINGS_DIR / "stops.rml.ttl"
STOP_KG_FILE = GRAPHS_DIR / "stops.nt"

ROUTE_FILE = DATA_DIR / "routes.txt"
ROUTE_RML_FILE = MAPPINGS_DIR / "routes.rml.ttl"
ROUTE_KG_FILE = GRAPHS_DIR / "routes.nt"

TRIP_FILE = DATA_DIR / "trips.txt"
TRIP_RML_FILE = MAPPINGS_DIR / "trips.rml.ttl"
TRIP_KG_FILE = GRAPHS_DIR / "trips.nt"

STOP_TIME_FILE = DATA_DIR / "stop_times.txt"
STOP_TIME_RML_FILE = MAPPINGS_DIR / "stop_times.rml.ttl"
STOP_TIME_KG_FILE = GRAPHS_DIR / "stop_times.nt"

# Namespaces
ONTOLOGY_PREFIX = "gtfs"
GTFS = Namespace(f"{gtfs_owl_iri}#")