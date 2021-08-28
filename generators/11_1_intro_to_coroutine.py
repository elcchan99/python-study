from libs.recvcount import recv_count


r = recv_count()
r.send(None)  # Note: must call .send(None) here

for i in range(5, 0, -1):
    r.send(i)
