#!/bin/bash

DIR_PATH="www/"

python gen_apache.py -o LOG -d $DIR_PATH --sleep 0.1 --num 100
python gen_apache.py -o LOG -d $DIR_PATH --sleep 0.1 --num 100
python gen_apache.py -o LOG -d $DIR_PATH --sleep 0.1 --num 100