from pathlib import Path

from libs.follow import follow

FILE = "www/follow.log"

Path(FILE).touch()

logfile = open(FILE)
loglines = follow(logfile)

for line in loglines:
    print(line, end="")
