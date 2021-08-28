import time

from libs.genmulti import multiplex


def range_sleep(*args, interval=1.0, prefix=""):
    for i in range(*args):
        time.sleep(interval)
        yield f"{prefix} {i}"


odd = range_sleep(1, 10, 1, prefix="from odd: ")
even = range_sleep(2, 20, 2, prefix="from even: ")


for y in multiplex([odd, even]):
    print(y)
