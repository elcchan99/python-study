class Consumer:
    name: str

    def __init__(self, name: str):
        self.name = name

    def send(self, item):
        print(self.name, "got", item)


def broadcast(source, consumers: list[Consumer]):
    for item in source:
        for c in consumers:
            c.send(item)
