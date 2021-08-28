# Generators

## Get started

Before running any scripts, install dependencies first.

```bash
poetry install
```

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

### 3. Fun with files and directories

Generate source data: apache logs

```bash
> python gen_apache.py -o LOG -d www/ --sleep 0.1 --num 1000
> python gen_apache.py -o LOG -d www/ --sleep 0.1 --num 250
> python gen_apache.py -o LOG -d www/ --sleep 0.1 --num 250
...
```

Create a generator to list all logs from directory

```python
>>> from linesdir import lines_from_dir
>>> lines = lines_from_dir(r"access_log_*.log", "www")
>>> next(lines)
>>> next(lines)
>>> next(lines)
```

### 4. Parsing and processing data

```python
>>> from linesdir import lines_from_dir
>>> from apachelog import apache_log
>>> lines = lines_from_dir(r"access_log_*.log", "www")
>>> logs = apache_log(lines)
>>> next(logs)
>>> next(logs)
>>> next(logs)
```

### 5. Processing infinite data

Open two terminals

One would follow on `www/follow.log` file

```bash
touch www/follow.log
python 05_01_follow.py
```

Another would add new lines to file

```bash
date >> www/follow.log
date >> www/follow.log
```

You shall see date print in the terminal which runs Python

### 6. Feeding the pipeline

- [Generate a sequence of TCP connections](./genreceive.py)
- [Receive a sequence of UDP messages](./genmessages.py)
