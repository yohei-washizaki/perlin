#!/usr/bin/env python3

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-a", type=float, nargs='+',
                        help="size of a texture. power of 2")
    parser.add_argument("-b", type=float, nargs='+',
                        help="size of a texture. power of 2")
    args = parser.parse_args()

    # if args.a:
    #     print(args.a)

    # if args.b:
    #     print(args.b)

    half = int(len(args.a) / 2)
    for i in range(0, half):
        c = args.a[i * 2] + args.b[i * 2]
        d = args.b[i * 2 + 1] + args.b[i * 2 + 1]

        print('{0} {1} '.format(c, d))
