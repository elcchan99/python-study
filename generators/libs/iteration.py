class counterdown_iter:
    count: int

    def __init__(self, count):
        self.count = count

    def __next__(self) -> int:
        if self.count <= 0:
            raise StopIteration
        r = self.count
        self.count -= 1
        return r


class countdown:
    start: int

    def __init__(self, start: int):
        self.start = start

    def __iter__(self):
        return counterdown_iter(self.start)
