from libs.cobroadcast import broadcast
from libs.cofollow import follow
from libs.grep import grep2
from libs.sinks import printer

open("follow.log", "a").close()


f = open("follow.log")
p = printer()
b = broadcast(
    targets=[
        grep2("python", target=p),
        grep2("python", target=p),
        grep2("2021", target=p),
        grep2("ply", target=p),
    ]
)
follow(f, target=b)
