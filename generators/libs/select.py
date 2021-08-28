from typing import Iterator, TypeVar


T = TypeVar("T")


def first(sources: Iterator[T], n: int = 1) -> Iterator[T]:
    for i, source in enumerate(sources):
        if i >= n:
            return
        yield source
