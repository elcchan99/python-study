import queue
import threading
from libs.genqueue import genfrom_queue


class ConsumerThread(threading.Thread):
    def __init__(self, target):
        super().__init__()
        self.setDaemon(True)
        self.in_q = queue.Queue()
        self.target = target

    def send(self, item):
        self.in_q.put(item)

    def run(self):
        self.target(genfrom_queue(self.in_q))
