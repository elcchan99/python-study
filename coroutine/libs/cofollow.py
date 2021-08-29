import os
import time
import typing


def follow(thefile: typing.IO, target: typing.Coroutine):
    thefile.seek(0, os.SEEK_END)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        target.send(line)
