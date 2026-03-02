# Start the REST endpoint
set output out
endpoint start

dstore create transit
active transit

prefix gtfs: <http://www.transit.ac.uk/ontologies/gtfs#>

import gtfs_tfwm.nt