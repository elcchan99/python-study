import xml.sax


class MyHandler(xml.sax.ContentHandler):
    def startElement(self, name, attrs):
        print("startElement", f"{name=}", f"{attrs=}")

    def endElement(self, name):
        print("endElement", f"{name=}")

    def characters(self, content):
        print("characters", f"{content=}")


xml.sax.parse("data/allroutes.xml", MyHandler())
