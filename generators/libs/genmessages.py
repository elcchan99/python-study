import socket


def receive_messages(addr, maxsize):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(addr)
    while True:
        msg = s.recvfrom(maxsize)
        yield msg


for msg, addr in receive_messages(("localhost", 10000), 1024):
    print(msg, "from", addr)
