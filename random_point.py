#!/usr/bin/env python3


def gen_random_points(num, scale_factor, random):
    random_points = []

    for i in range(num):
        x = random.random() * scale_factor
        y = random.random() * scale_factor
        random_points.append((x, y))

    return random_points


if __name__ == "__main__":
    import argparse
    import random
    
    parser = argparse.ArgumentParser()
    parser.add_argument("num", type=int, help="number of points generated")
    parser.add_argument("-r", "--random_seed", type=int, help="random seed")
    parser.add_argument("-s", "--scale_factor", type=float, default=1.0, help="scale factor")
    args = parser.parse_args()

    random.seed(args.random_seed)
    random_points = gen_random_points(args.num, args.scale_factor, random)

    for point in random_points:
        print('{0[0]:.15f} {0[1]:.15f}'.format(point, point))
