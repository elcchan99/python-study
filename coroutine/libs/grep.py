import typing


def grep(pattern: str) -> typing.Coroutine:
    print(f"Looking for {pattern}")
    while True:
        line = yield
        if pattern in line:
            print(line)
