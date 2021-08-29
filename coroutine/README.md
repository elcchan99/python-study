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
