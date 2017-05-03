#!/usr/bin/env python3

import argparse
import fileinput
import util

parser = argparse.ArgumentParser()
parser.add_argument("size", type=int, help="size of a texture. power of 2")
args = parser.parse_args()

power_of_2_size = util.next_power_of_2(args.size)
print(power_of_2_size)
