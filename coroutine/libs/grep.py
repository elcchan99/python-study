import typing
from .coroutine import coroutine


def raw_grep(pattern: str) -> typing.Coroutine:
    print(f"Looking for {pattern}")
    while True:
        line = yield
        if pattern in line:
            print(line)


@coroutine
def grep(pattern: str) -> typing.Coroutine:
    print(f"Looking for {pattern}")
    while True:
        line = yield
        if pattern in line:
            print(line)


@coroutine
def grep2(pattern: str, target: typing.Coroutine):
    while True:
        line = yield
        if pattern in line:
            target.send(line)
