from libs.storelast import storelast

numbers = (i for i in range(4))
numbers = storelast(numbers)

for n in numbers:
    print("current", n)
    print("generator.last", numbers.last)
