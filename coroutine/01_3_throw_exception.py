from libs.grep import grep


g = grep("python")

g.send("ptthon generators tocks!")

g.throw(RuntimeError, "You're hosed")
