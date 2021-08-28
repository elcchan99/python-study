def gen_countdown(n: int):
    print("Counting down from", n)
    while n > 0:
        yield n
        n -= 1


g = gen_countdown(5)
print(g)
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
