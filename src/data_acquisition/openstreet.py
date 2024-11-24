"""Module for collection data from OpenStreetMaps"""

from OSMPythonTools.overpass import Overpass

# Initiate OSM
ovr_pass = Overpass()

# set area of interest
query = ovr_pass.query('''
                       area[name='Salt Lake City'];
                       (way[]"highway"](area));
                           (._;>;);
    												out body;
                       ''')

# Validate
print(query.countElements())  # Total elements fetched
print(query.elements()[0])    # Example: First element details
