from follow import follow

logfile = open("www/follow.log")
loglines = follow(logfile)

for line in loglines:
    print(line, end="")
