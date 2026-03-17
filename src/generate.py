from config import GTFS_ONTOLOGY_RDF
from core import gtfs
import agencies
import stops
import routes

gtfs.save(file=str(GTFS_ONTOLOGY_RDF))