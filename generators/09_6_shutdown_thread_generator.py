import threading
import time
from typing import Optional


def count(n, shutdown: Optional[threading.Event] = None):
    for i in range(n):
        if shutdown and shutdown.is_set():
            break
        yield i
        time.sleep(0.1)


shutdown = threading.Event()


def count_number(n, shutdown):
    nums = count(n, shutdown)
    for n in nums:
        print(n)


thr = threading.Thread(target=count_number, args=(20, shutdown))
thr.start()

time.sleep(0.5)

print("Closing it down")
shutdown.set()
