#!/usr/bin/env python3


import util


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
        n = util.normalize_vector(v[0], v[1])
        normalized.append(n)

    return normalized


def perlin(aa, ab, ba, bb, x, y, unit_vectors):
    aav = unit_vectors[aa]
    abv = unit_vectors[ab]
    bav = unit_vectors[ba]
    bbv = unit_vectors[bb]
    aap = (x, y)
    bap = (x - 1, y)
    abp = (x, y - 1)
    bbp = (x - 1, y - 1)
    return util.lerp(
        util.lerp(grad(aav, aap), grad(bav, bap), util.fade(x)),
        util.lerp(grad(abv, abp), grad(bbv, bbp), util.fade(x)),
        util.fade(y))


def grad(grad_vector, position_vector):
    return util.dot_vector(grad_vector, position_vector)


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
