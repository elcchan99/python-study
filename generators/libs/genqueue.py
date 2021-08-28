import queue
from typing import Iterator, TypeVar, Union

T = TypeVar("T")


def sendto_queue(source: Iterator[T], thequeue: queue.Queue[Union[T, StopIteration]]):
    for item in source:
        thequeue.put(item)
    thequeue.put(StopIteration)


def genfrom_queue(thequeue: queue.Queue[Union[T, StopIteration]]) -> Iterator[T]:
    while True:
        item = thequeue.get()
        if item is StopIteration:
            break
        yield item
