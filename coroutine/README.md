# Coroutine

## Get started

Before running any scripts, install dependencies first.

```bash
poetry install
```

## A Curious Course on Coroutines and Concurrency

Author: David Beazley

Presented at PyCon'2009, Chicago, Illinois

Source: https://www.eecg.utoronto.ca/~jzhu/csc326/readings/Coroutines.pdf

### 1. Intro to Coroutines

#### 1.1 grep sample

We need to call `grep.__next__()` to kick start it.

```shell
> python 01_1_grep_coroutine.py
Looking for python
python generators rock!
```

#### 1.2 decorated coroutine

We call `next(coroutine)` in decorator.

```shell
> python 01_2_decorated_coroutine.py
Looking for python
python generators rock!
```

#### 1.3 throwing an exception

We could raise an exception, which originates at the yield expression.
This kind of exception can be caught/ handled in the usual ways.

```shell
> python 01_3_throw_exception.py
Looking for python
Traceback (most recent call last):
  File "/Users/edgarchan/personal/python-study/coroutine/01_3_throw_exception.py", line 8, in <module>
    g.throw(RuntimeError, "You're hosed")
  File "/Users/edgarchan/personal/python-study/coroutine/libs/grep.py", line 17, in grep
    line = yield
RuntimeError: You're hosed
```
