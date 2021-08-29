import xml.sax

from libs.buses import buses_to_dict
from libs.cosax import EventHandler
from libs.coroutine import coroutine


@coroutine
def printer():
    while True:
        item = yield
        print(item)


co_print = printer()
co_to_dict = buses_to_dict(target=co_print)

handler = EventHandler(target=co_to_dict)
xml.sax.parse("data/allroutes.xml", handler)
