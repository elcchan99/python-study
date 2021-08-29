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

#### 1.4 generator that produces and receives

It runs, but its

```shell
> python 01_4_bogus_example.py
Counting down from 5
5
2
1
0
```

### 2. Coroutines, pipeline and dataflow

#### 2.1 sample pipeline

`follow |> printer`

Open two terminals

1. One starts to tail the file `follow.log`
   ```bash
   python 02_1_follow_print.py
   ```
1. Another pushes some lines to the file
   ```bash
   date >> follow.log
   date >> follow.log
   ```

Result

```shell
> python 02_1_follow_print.py
Sun Aug 29 12:14:29 HKT 2021
Sun Aug 29 12:14:46 HKT 2021
```

#### 2.2 add filter

Open two terminals

1. One starts to tail the file `follow.log`
   ```bash
   python 02_1_follow_print.py
   ```
2. Another pushes some lines to the file:
   ```bash
   date >> follow.log
   echo "python rocks!" >> follow.log
   date >> follow.log
   ```

Result: only `python rocks!` is printed

```shell
> python 02_2_filter.py
python rocks
```

#### 2.3 broadcasting

Open two terminals

1. One starts to tail the file `follow.log`
   ```bash
   python 02_3_broadcast.py
   ```
2. Another pushes some lines to the file:
   ```bash
   echo "python rocks" >> follow.log
   date >> follow.log
   echo "ply ply ply" >> follow.log
   ```

Result

```shell
> python 02_3_broadcast.py
python rocks
python rocks
Sun Aug 29 12:41:26 HKT 2021
ply ply ply
```

### 3. Coroutines and Event dispatching

#### 3.1 minimal SAX example

```shell
> python 03_1_sample_xml_sax.py
```

#### 3.2 parse bus event

Parse xml to turn bus XML to dictionary

```shell
> python 03_2_bus_event_dispatch.py
```

#### 3.3 parse bus event and filter

```shell
> python 03_3_bus_event_dispatch_filter.py
```

#### 3.4 threaded

Two threads

1. xml -> EventHandler -> buses_to_dicts
2. filter_on_field -> filter_on_field -> bus_locations

```shell
> python 03_4_threaded_bus_event.py
```

#### 3.5 bridge coroutines over a file/ pipe

See `libs/coprocess.py`.

This has high cost of the underlying communication.
