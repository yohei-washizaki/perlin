#!/usr/bin/env python3

def proc(s, bias):
    xy = s.split(' ')
    x = float(xy[0]) * bias
    y = float(xy[1]) * bias
    print('{0} {1}'.format(x, y))


if __name__ == "__main__":
    import argparse
    import sys
    import util

    parser = argparse.ArgumentParser()
    parser.add_argument("size", type=int, help="size of a texture. power of 2")
    args = parser.parse_args()

    grid_size = util.power_to_int(args.size)

    for line in sys.stdin:
        proc(line.strip(), grid_size)
