#!/usr/bin/env python3
import math


def split_float(x):
    xf, xi = math.modf(float(x))
    return int(xi), xf


if __name__ == "__main__":
    import sys
    
    for line in sys.stdin:
        s = line.strip()
        xy = s.split(' ')
        x = split_float(xy[0])
        y = split_float(xy[1])
        print('{0[0]} {1[0]} {0[1]:.8f} {1[1]:.8f}'.format(x, y))
