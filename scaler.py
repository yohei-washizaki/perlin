#!/usr/bin/env python3


def apply_scale(xy, scale):
    x = float(xy[0]) * scale
    y = float(xy[1]) * scale
    print('{0} {1}'.format(x, y))


if __name__ == "__main__":
    import argparse
    import sys
    import util

    parser = argparse.ArgumentParser()
    parser.add_argument("scale", type=int, help="Scale to apply")
    args = parser.parse_args()

    grid_size = util.power_to_int(args.scale)

    for line in sys.stdin:
        s = line.strip()
        xy = s.split(' ')
        apply_scale(xy, grid_size)
