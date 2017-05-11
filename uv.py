#!/usr/bin/env python3


def gen_uv(width, height, scale=1.0):
    w_inv = 1.0 / width
    h_inv = 1.0 / height
    uv = []
    for h in range(height):
        for w in range(width):
            u = (w + 0.5) * w_inv * scale
            v = (h + 0.5) * h_inv * scale
            uv.append((u, v))

    return uv


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("size", type=int, help="size of a texture. power of 2")
    args = parser.parse_args()

    uvs = gen_uv(args.size, args.size)

    for uv in uvs:
        print('{0[0]} {0[1]}'.format(uv))
