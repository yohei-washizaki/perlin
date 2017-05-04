#!/usr/bin/env python3


import math


def normalize_vector(x, y):
    length = math.sqrt(x * x + y * y)

    if math.isclose(length, 0):
        return (x, y)
    else:
        inv = 1.0 / length
        return (x * inv, y * inv)


def dot_vector(v1, v2):
    return v1[0] * v2[0] + v1[1] * v2[1]


def create_unitvectors():
    unnormalized = [
        (1, 0),
        (1, 1),
        (0, 1),
        (-1, 1),
        (-1, 0),
        (-1, -1),
        (0, -1),
        (1, -1),
    ]
    normalized = []
    for v in unnormalized:
        n = normalize_vector(v[0], v[1])
        normalized.append(n)

    return normalized


def fade(t):
    return t * t * t * (t * (t * 6 - 15) + 10)


def lerp(a, b, t):
    return a + t * (b - a)


def perlin(aa, ab, ba, bb, x, y, unit_vectors):
    aav = unit_vectors[aa]
    abv = unit_vectors[ab]
    bav = unit_vectors[ba]
    bbv = unit_vectors[bb]
    aap = (x, y)
    bap = (x - 1, y)
    abp = (x, y - 1)
    bbp = (x - 1, y - 1)
    return lerp(
        lerp(grad(aav, aap), grad(bav, bap), fade(x)),
        lerp(grad(abv, abp), grad(bbv, bbp), fade(x)),
        fade(y))


def grad(grad_vector, position_vector):
    return dot_vector(grad_vector, position_vector)


def bind(v):
    return (v + 1.0) * 0.5


if __name__ == "__main__":
    import sys

    unit_vectors = create_unitvectors()

    for line in sys.stdin:
        params = line.strip().split(' ')
        aa = int(params[0])
        ab = int(params[1])
        ba = int(params[2])
        bb = int(params[3])
        x = float(params[4])
        y = float(params[5])

        p = bind(perlin(aa, ab, ba, bb, x, y, unit_vectors))
        print('{0}'.format(p))
