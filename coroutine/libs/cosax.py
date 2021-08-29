import xml.sax
import typing


class Message(typing.NamedTuple):
    type: str
    value: typing.Any


class EventHandler(xml.sax.ContentHandler):
    def __init__(self, target: typing.Coroutine) -> None:
        self.target = target

    def startElement(self, name, attrs):
        msg = Message(type="start", value=(name, attrs._attrs))
        self.target.send(msg)

    def characters(self, content):
        msg = Message(type="text", value=content)
        self.target.send(msg)

    def endElement(self, name):
        msg = Message(type="end", value=name)
        self.target.send(msg)
