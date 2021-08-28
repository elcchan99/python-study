from typing import Iterator, TypeVar


T = TypeVar("T")

def gen_cat(sources: Iterator[T]) -> Iterator[T]:
    for src in sources:
        yield from src