#!/usr/bin/env python3
import math


def calc_sqr_distance(a, b):
    vx = a[0] - b[0]
    vy = a[1] - b[1]
    return vx * vx + vy * vy


def find_nearest_distance(uv, max_size, random_points):
    xf, xi = math.modf(uv[0])
    yf, yi = math.modf(uv[1])

    min_sqr_distance = float("inf")
    
    for y_offset in [-1, 0, 1]:
        for x_offset in [-1, 0, 1]:
            x = int((xi + x_offset + max_size) % max_size)
            y = int((yi + y_offset + max_size) % max_size)
            
            idx = int(x * max_size + y)
            p = random_points[idx]
            other = (x_offset + xi + p[0],
                     y_offset + yi + p[1])

            sqr_distance = calc_sqr_distance(uv, other)
            if sqr_distance < min_sqr_distance:
                min_sqr_distance = sqr_distance
                
    return math.sqrt(min_sqr_distance)

if __name__ == "__main__":
    import argparse
    import random
    from random_point import gen_random_points
    from uv import gen_uv

    parser = argparse.ArgumentParser()
    parser.add_argument("size", type=int, help="size of a texture. power of 2")
    parser.add_argument("-r", "--random_seed", type=int, help="random seed")
    parser.add_argument("-s", "--scale_factor", type=float, default=1.0, help="scale factor")
    args = parser.parse_args()

    scale_factor = args.scale_factor
    
    random.seed(args.random_seed)
    random_points = gen_random_points(int(scale_factor*scale_factor), 1.0, random)
    
    uvs = gen_uv(args.size, args.size, scale_factor)

    for uv in uvs:
        nearest_distance = find_nearest_distance(uv, scale_factor, random_points)
        print(nearest_distance)

