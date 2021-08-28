from libs.consumercoroutine import consumer
from libs.recvcount import recv_count


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
