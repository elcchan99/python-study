import queue
import threading
import typing

from libs.coroutine import coroutine


@coroutine
def threaded(target: typing.Coroutine):
    message = queue.Queue()

    def run_target():
        while True:
            item = message.get()
            if item is GeneratorExit:
                target.close()
                return
            target.send(item)

    thr = threading.Thread(target=run_target)
    thr.start()

    try:
        while True:
            item = yield
            message.put(item)
    except GeneratorExit:
        message.put(GeneratorExit)
