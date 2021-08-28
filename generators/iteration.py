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


def gen_countdown(n: int):
    print("Counting down from", n)
    while n > 0:
        yield n
        n -= 1


if __name__ == "__main__":
    print("Iterator version of countdown:")
    for i in countdown(5):
        print(i, end=" ")
    print()

    print("Generator version of countdown:")
    g = gen_countdown(5)
    print(g)
    print(g.__next__())
    print(g.__next__())
    print(g.__next__())
    print(g.__next__())
    print(g.__next__())
    print(g.__next__())
