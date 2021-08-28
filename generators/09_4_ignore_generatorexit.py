import os
import time


def follow(thefile):
    # thefile.seek(0, os.SEEK_END)
    try:
        while True:
            line = thefile.readline()
            if not line:
                time.sleep(0.1)  # Sleep briefly
                continue
            yield line
    except GeneratorExit:
        print("Follow: Shutting down")


lines = follow(open("www/follow.log"))
for i, line in enumerate(lines):
    print(line, end="")
    if i == 0:
        lines.close()
