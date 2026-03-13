from config import GTFS_ONTOLOGY_RDF
from core import gtfs
import agencies

gtfs.save(file=str(GTFS_ONTOLOGY_RDF))