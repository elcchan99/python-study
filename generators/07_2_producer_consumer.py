import queue
import threading

from libs.apachelog import apache_log
from libs.genqueue import genfrom_queue, sendto_queue
from libs.linesdir import lines_from_dir

# consumer
def print_r4040(log_q: queue.Queue):
    log = genfrom_queue(log_q)
    r404 = (r for r in log if r["status"] == 404)
    for r in r404:
        print(r["host"], r["datetime"], r["request"])


# consumer driver
log_q = queue.Queue()
r404_thr = threading.Thread(target=print_r4040, args=(log_q,))
r404_thr.start()

# producer
lines = lines_from_dir("access_log*.log", "www")
logs = apache_log(lines)
sendto_queue(logs, log_q)
