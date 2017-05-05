#!/usr/bin/env python3
from PIL import Image
import sys


def float_to_rgb(v):
    color = int(round(v * 255))
    return (color, color, color)


def estimate_size(buf):
    import math
    side = int(math.sqrt(len(buf)))
    return (side, side)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=str, help="output file name")
    args = parser.parse_args()

    colors = []
    for line in sys.stdin:
        colors.append(float(line.strip()))
        # colors.append(float_to_rgb(float(line.strip())))

    sz = estimate_size(colors)

    img = Image.new("L", sz)
    for y in range(sz[0]):
        for x in range(sz[1]):
            index = x + sz[0] * y
            c = int(colors[index] * 255)

            xb = x
            yb = sz[0] - y - 1
            img.paste(c, (xb, yb, xb + 1, yb + 1))

    img.save(args.output)
