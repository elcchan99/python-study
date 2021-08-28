from libs.recvcount import recv_count


def consumer(func):
    def start(*args, **kwargs):
        c = func(*args, **kwargs)
        c.send(None)
        return c

    return start


@consumer
def recv_count():
    try:
        while True:
            n = yield  # Yield expression
            print("T-minus", n)
    except GeneratorExit:
        print("Kaboom!")


r = recv_count()
for i in range(5, 0, -1):
    r.send(i)

print("...")
