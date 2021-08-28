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
