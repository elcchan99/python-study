import threading
import time


def count(n):
    for i in range(n):
        yield i
        time.sleep(0.01)


numbers = count(20)


def sleep_and_close(t):
    time.sleep(t)
    numbers.close()


thr = threading.Thread(target=sleep_and_close, args=(0.1,))
thr.start()

for line in numbers:
    print(line)
