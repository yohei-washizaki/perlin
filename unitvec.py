#!/usr/bin/env python3
import math
import argparse
import util

parser = argparse.ArgumentParser()
parser.add_argument("size", type=int, help="size of a texture. power of 2")
args = parser.parse_args()

power_of_2_size = util.next_power_of_2(args.size)
print(power_of_2_size)

for i in range(power_of_2_size):
    f = float(i) / power_of_2_size
    r = math.radians(360 * f)
    c = math.cos(r)
    s = math.sin(r)
    print('{0:.8f} {1:.8f}'.format(c, s))
