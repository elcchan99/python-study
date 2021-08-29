import xml.sax

from libs.buses import bus_locations, buses_to_dict, filter_on_field
from libs.cosax import EventHandler
from libs.cothread import threaded


filters = filter_on_field(
    fieldname="route",
    value="22",
    target=filter_on_field(
        fieldname="direction", value="North Bound", target=bus_locations()
    ),
)
threaded_filters = threaded(filters)
co_to_dict = buses_to_dict(target=threaded_filters)

handler = EventHandler(target=co_to_dict)
xml.sax.parse("data/allroutes.xml", handler)

threaded_filters.close()
