import pickle
import typing
from libs.coroutine import coroutine


@coroutine
def sendto(f: typing.IO):
    try:
        while True:
            item = yield
            pickle.dump(item, f)
            f.flush()
    except StopIteration:
        f.close()


def recvfrom(f: typing.IO, target: typing.Coroutine):
    try:
        while True:
            item = pickle.loads(f)
            target.send(item)
    except EOFError:
        target.close()
