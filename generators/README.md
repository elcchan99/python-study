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

Iteration of `countdown`

```bash
python 01_1_run_iterator.py
```

### 2. Introduction to generators

Iterate a generator version of `countdown`

```bash
python 02_1_run_generator.py
```

### 3. Fun with files and directories

Generate source data: apache logs

```bash
bash 03_1_generate_data.sh
```

Create a generator to list logs from directory

```bash
python 03_2_read_from_dir.py
```

### 4. Parsing and processing data

Run the below commands to parse apache log from string to dict

```bash
python 04_1_parse_apache.py
```

### 5. Processing infinite data

Open two terminals

One would follow on `www/follow.log` file

```bash
python 05_1_follow.py
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

### 7. Extending the pipeline

#### 7.1 Sender and receiver

Open two terminals

One would start a consumer that listens to localhost:15000

```bash
python 07_1_consumer.py
```

Another would send apache log dict to localost:15000

```bash
python 07_1_producer.py
```

You would see apache log dict is printed in consumer terminal.

#### 7.2 Multiple threads

```bash
python 07_2_producer_consumer.py
```

### 8 Advanced data routing

Parallel iteration

marginally useful:

```python
s1 = range(1, 10)
s2 = range(2, 10, 2)
s3 = range(3, 10, 3)
z = zip(s1, s2, s3)
for e in z:
    print(e)
```

#### 8.1 Multiplexing

- multiple generators
- real time productin values as they arrive

```shell
> python 08_1_multiplex.py
from odd:  1
from even:  2
from odd:  2
from even:  4
from odd:  3
from even:  6
from odd:  4
from even:  8
from odd:  5
from even:  10
from odd:  6
from even:  12
from odd:  7
from even:  14
from odd:  8
from even:  16
from odd:  9
from even:  18
```

With the `time.sleep`, you can see the result generator takes value from sources interchangablely.

#### 8.2 Broadcasting

```shell
> python 08_2_broadcast.py
Ada got 155.218.119.91
Bob got 155.218.119.91
Cat got 155.218.119.91
Ada got 206.229.250.64
Bob got 206.229.250.64
Cat got 206.229.250.64
Ada got 213.190.121.174
Bob got 213.190.121.174
Cat got 213.190.121.174
```
