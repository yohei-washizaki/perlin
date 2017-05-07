#!/usr/bin/env python3

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("size", type=int, help="size of a texture. power of 2")
    args = parser.parse_args()

    for h in range(args.size):
        for w in range(args.size):
            print('0 0')
