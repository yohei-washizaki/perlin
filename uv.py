#!/usr/bin/env python3

#import random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("size", type=int, help="size of a texture. power of 2")
#parser.add_argument("scale", type=float, help="scale")
parser.add_argument("-s", "--seed", type=int, help="random seed")
args = parser.parse_args()

# random.seed(args.seed)

uvs = []
inv = 1.0 / args.size
for h in range(args.size):
    for w in range(args.size):
        u = (w + 0.5) * inv
        v = (h + 0.5) * inv
        print('{0} {1}'.format(u, v))
