import time
import os
import typing


def follow(thefile: typing.IO) -> typing.Iterator[str]:
    """Equivalent to tail -f"""
    thefile.seek(0, os.SEEK_END)  # End-of-file
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)  # Sleep briefly
            continue
        yield line
