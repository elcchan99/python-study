import os

from libs.cofollow import follow
from libs.coroutine import coroutine


@coroutine
def printer():
    while True:
        line = yield
        print(line, end="")


# touch file
open("follow.log", "a").close()

file = open("follow.log")
lines = follow(file, target=printer())
