from libs.cofollow import follow
from libs.sinks import printer


# touch file
open("follow.log", "a").close()

file = open("follow.log")
follow(file, target=printer())
