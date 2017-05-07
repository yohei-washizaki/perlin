#!/usr/bin/env python3
import util
from perlin import Perlin
from perlin import UnitVectors
from perlin import grad
from perlin import bind


class OctaveNoise(Perlin):
    """Octave perlin noise"""

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

        return noise


if __name__ == "__main__":
    import sys
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("unitvectors",
                        type=float, nargs='+',
                        help="whitespace separated unit vectors list")
    parser.add_argument("-o", "--octaves",
                        type=int, default=8,
                        help="octaves")
    args = parser.parse_args()

    unit_vectors = UnitVectors(args.unitvectors)
    noise_generator = OctaveNoise()

    for line in sys.stdin:
        params = line.strip().split(' ')
        aa = int(params[0])
        ab = int(params[1])
        ba = int(params[2])
        bb = int(params[3])
        x = float(params[4])
        y = float(params[5])

        p = noise_generator.generate_noise(aa, ab, ba, bb, x, y, unit_vectors)
        print('{0}'.format(p))
