import socket


def receive_connection(addr: tuple[str, int]):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(addr)
    s.listen(5)
    while True:
        client = s.accept()
        yield client


for c, a in receive_connection(("localhost", 9000)):
    c.send(b"Hello World\n")
    c.close()
