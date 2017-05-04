#!/usr/bin/env python3
import math


def next_power_of_2(x):

    if x == 1:
        return 1

    if x == 2:
        return 4

    return int(math.pow(2, math.ceil(math.log2(float(x)))))


def power_to_int(x):

    return int(math.pow(x, 2))


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--powerof2", type=int, help="power of 2")
    parser.add_argument("--power", type=int, help="power")
    args = parser.parse_args()

    if args.powerof2:
        print(next_power_of_2(args.powerof2))
    elif args.power:
        print(power_to_int(args.power))
