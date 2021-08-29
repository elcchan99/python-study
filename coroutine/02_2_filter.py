from libs.cofollow import follow
from libs.grep import grep2
from libs.sinks import printer

open("follow.log", "a").close()

f = open("follow.log")
g = grep2("python", printer())
follow(f, target=g)
