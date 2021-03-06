import socket

from .genpickle import gen_unpickle


def receivefrom(addr: tuple[str, int]):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(addr)
    s.listen(5)
    c, _ = s.accept()
    for item in gen_unpickle(c.makefile("rb")):
        yield item
    c.close()
