import sys

from libs import select
from libs.apachelog import apache_log
from libs.broadcast import broadcast
from libs.linesdir import lines_from_dir
from libs.thrsend import ConsumerThread


def find_404(logs):
    logs_404 = (r for r in logs if r["status"] == 404)
    for r in logs_404:
        print(r["status"], r["datetime"], r["request"])


def bytes_transferred(logs):
    total = 0
    for r in logs:
        total += r["bytes"]
        print("Total bytes", total)


c1 = ConsumerThread(find_404)
c1.start()
c2 = ConsumerThread(bytes_transferred)
c2.start()

lines = lines_from_dir("access_log*.log", "www")
logs = apache_log(lines)
logs = select.first(logs, 50)

broadcast(logs, [c1, c2])

c1.join()
c2.join()

print("Hi")
sys.exit(0)
