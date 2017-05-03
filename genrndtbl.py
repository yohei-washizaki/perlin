#!/usr/bin/env python3

import argparse
import random

parser = argparse.ArgumentParser()
parser.add_argument("length", type=int, help="length of a table")
parser.add_argument("-s", "--seed", type=int, help="random seed")
args = parser.parse_args()

random.seed(args.seed)

x = []
for i in range(args.length):
    x.append(i)

random.shuffle(x)

for i in x:
    print(i)
