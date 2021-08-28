# Generators

## Generator Tricks For Systems Programmers

Author: David Beazley
Originally Presented at PyCon 2008
Updated: October, 2018
Link: http://www.dabeaz.com/generators/Generators.pdf

### 1. Basic iteration protocol

```shell
python iteration.py
5 4 3 2 1
```

### 2. Introduction to generators

```shell
python iteration.py
<generator object gen_countdown at 0x1101bcba0>
Counting down from 5
5
4
3
2
1
Traceback (most recent call last):
  File "generators/iteration.py", line 45, in <module>
    print(g.__next__())
StopIteration
```
