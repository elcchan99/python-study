from typing import Callable, Generator


def consumer(func: Callable[[], Generator]):
    def start(*args, **kwargs):
        c = func(*args, **kwargs)
        c.send(None)
        return c

    return start
