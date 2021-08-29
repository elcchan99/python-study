import typing

from libs.coroutine import coroutine


@coroutine
def broadcast(targets: list[typing.Coroutine]):
    while True:
        value = yield
        for t in targets:
            t.send(value)
