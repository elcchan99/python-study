from libs.grep import raw_grep

g = raw_grep("python")

g.__next__()
g.send("Yeah, but no, but yeah, but no")
g.send("A series of tubes")
g.send("python generators rock!")
