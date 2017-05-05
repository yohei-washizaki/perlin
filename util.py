#!/usr/bin/env python3
import math


def normalize_vector(x, y):
    length = math.sqrt(x * x + y * y)

    if math.isclose(length, 0):
        return (x, y)
    else:
        inv = 1.0 / length
        return (x * inv, y * inv)


def dot_vector(v1, v2):
    return v1[0] * v2[0] + v1[1] * v2[1]


def fade(t):
    return t * t * t * (t * (t * 6 - 15) + 10)


def lerp(a, b, t):
    return a + t * (b - a)



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
