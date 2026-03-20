from pathlib import Path

from gtfs_ontology.generate import generate_ontology

generate_ontology(
    path=Path(__file__).parent / "gtfs.rdf"
)