#!/usr/bin/env python3
import math


def create_unitvectors(n):
    step = 360.0 / n
    for i in range(n):
        radian = math.radians(i * step)
        print('{0:.16f} {1:.16f}'.format(math.cos(radian), math.sin(radian)))


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("count", type=int, help="count of created vectors.")
    args = parser.parse_args()
    
    create_unitvectors(args.count)
