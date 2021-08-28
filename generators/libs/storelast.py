class storelast:
    def __init__(self, source):
        self.source = source

    def __next__(self):
        item = self.source.__next__()
        self.last = item
        return item

    def __iter__(self):
        return self
