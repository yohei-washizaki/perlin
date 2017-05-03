#!/usr/bin/env python3
import math
import argparse


def next_power_of_2(x):

    return int(math.pow(2, math.ceil(math.log2(x))))


parser = argparse.ArgumentParser()
parser.add_argument("size", type=int, help="size of a texture. power of 2")
args = parser.parse_args()

power_of_2_size = next_power_of_2(args.size)
print(power_of_2_size)

for i in range(power_of_2_size):
    f = float(i) / power_of_2_size
    r = math.radians(360 * f)
    c = math.cos(r)
    s = math.sin(r)
    print('{0:.8f} {1:.8f}'.format(c, s))
