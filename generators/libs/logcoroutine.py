from .consumercoroutine import consumer


@consumer
def find_404():
    while True:
        r = yield
        if r["status"] == 404:
            print(r["status"], r["datetime"], r["request"])


@consumer
def bytes_transferred():
    total = 0
    while True:
        r = yield
        total += r["bytes"]
        print("Total bytes", total)
