#!/usr/bin/env python3
import util


def grad(grad_vector, position_vector):
    return util.dot_vector(grad_vector, position_vector)


def bind(v, min_value, max_value):
    scalar = max_value - min_value
    half = scalar * 0.5
    return (v + scalar) * half


class Perlin:
    """Generate perlin noise"""

    def generate_noise(self, aa, ab, ba, bb, x, y, unit_vectors):
        aav = unit_vectors[aa]
        abv = unit_vectors[ab]
        bav = unit_vectors[ba]
        bbv = unit_vectors[bb]
        aap = (x, y)
        abp = (x, y - 1)
        bap = (x - 1, y)
        bbp = (x - 1, y - 1)

        noise = util.lerp(
            util.lerp(grad(aav, aap), grad(bav, bap), util.fade(x)),
            util.lerp(grad(abv, abp), grad(bbv, bbp), util.fade(x)),
            util.fade(y))

        return bind(noise, 0, 1)


class UnitVectors:
    """List of unit vectors"""

    def __init__(self, vectors):
        self.vectors = self.parse_vectors(vectors)

    def parse_vectors(self, vectors):
        v = []

        count = int(len(vectors) / 2)
        for i in range(count):
            v.append((vectors[i * 2], vectors[(i * 2) + 1]))

        return v

    def __getitem__(self, k):
        return self.vectors[k % len(self.vectors)]


if __name__ == "__main__":
    import sys
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("unitvectors",
                        type=float, nargs='+',
                        help="whitespace separated unit vectors list")
    args = parser.parse_args()

    unit_vectors = UnitVectors(args.unitvectors)
    perlin = Perlin()

    for line in sys.stdin:
        params = line.strip().split(' ')
        aa = int(params[0])
        ab = int(params[1])
        ba = int(params[2])
        bb = int(params[3])
        x = float(params[4])
        y = float(params[5])

        p = perlin.generate_noise(aa, ab, ba, bb, x, y, unit_vectors)
        print('{0}'.format(p))
