import typing
from .coroutine import corotine


def raw_grep(pattern: str) -> typing.Coroutine:
    print(f"Looking for {pattern}")
    while True:
        line = yield
        if pattern in line:
            print(line)


@corotine
def grep(pattern: str) -> typing.Coroutine:
    print(f"Looking for {pattern}")
    while True:
        line = yield
        if pattern in line:
            print(line)
