#!/usr/bin/env python3
import random


def generate_random_table(length, seed):
    random.seed(seed)

    x = []
    for i in range(length):
        x.append(i)
    random.shuffle(x)
    return x


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("length", type=int, help="length of a table")
    parser.add_argument("-s", "--seed", type=int, help="random seed")
    args = parser.parse_args()

    x = generate_random_table(args.length, args.seed)

    for i in x:
        print(i)
