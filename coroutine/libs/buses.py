import typing

from libs.coroutine import coroutine


@coroutine
def buses_to_dict(target: typing.Coroutine):
    while True:
        event, value = yield
        # Look for the start of <bus> element
        if event == "start" and value[0] == "bus":
            busdict = {}
            fragments = []
            # Capture text of inner elements in a dict
            while True:
                event, value = yield
                if event == "start":
                    fragments = []
                elif event == "text":
                    fragments.append(value)
                elif event == "end":
                    if value != "bus":
                        busdict[value] = "".join(fragments)
                    else:
                        target.send(busdict)
                        break
