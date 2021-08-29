from libs.coroutine import coroutine


@coroutine
def printer():
    while True:
        line = yield
        print(line, end="")
