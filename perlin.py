#!/usr/bin/env python3
import util
import splitfloat
import hash


def grad(grad_vector, position_vector):
    return util.dot_vector(grad_vector, position_vector)


def bind(v, min_value, max_value):
    scalar = max_value - min_value
    half = scalar * 0.5
    return (v + scalar) * half


class PerlinNoise:
    """Generate perlin noise"""

    def generate(self, x, y, freq, hash_table, unit_vectors):
        xi, xf = splitfloat.split_float(x)
        yi, yf = splitfloat.split_float(y)

        xim = xi % freq
        xjm = (xi + 1) % freq
        yim = yi % freq
        yjm = (yi + 1) % freq

        aa = hash_table.hash(hash_table.hash(xim) + yim)
        ab = hash_table.hash(hash_table.hash(xim) + yjm)
        ba = hash_table.hash(hash_table.hash(xjm) + yim)
        bb = hash_table.hash(hash_table.hash(xjm) + yjm)

        aav = unit_vectors[aa]
        abv = unit_vectors[ab]
        bav = unit_vectors[ba]
        bbv = unit_vectors[bb]
        aap = (xf, yf)
        abp = (xf, yf - 1)
        bap = (xf - 1, yf)
        bbp = (xf - 1, yf - 1)

        noise = util.lerp(
            util.lerp(grad(aav, aap), grad(bav, bap), util.fade(xf)),
            util.lerp(grad(abv, abp), grad(bbv, bbp), util.fade(xf)),
            util.fade(yf))

        return bind(noise, 0, 1)


if __name__ == "__main__":
    import sys
    import argparse
    import unitvec

    parser = argparse.ArgumentParser()
    parser.add_argument("frequency",
                        type=int, help="frequency")
    parser.add_argument("-n", "--num_vectors",
                        type=int, default=8,
                        help="number of vectors generated")
    parser.add_argument("-l", "--hashtable_length",
                        type=int, default=256,
                        help="specify length of hash table")
    parser.add_argument("-r", "--random_seed",
                        type=int,
                        help="specify random seed")
    args = parser.parse_args()

    unit_vectors = unitvec.UnitVectors.Create(args.num_vectors)
    hash_table = hash.HashTable.Create(args.hashtable_length, args.random_seed)
    perlin_noise = PerlinNoise()
    freq = args.frequency
    for line in sys.stdin:
        params = line.strip().split(' ')
        x = float(params[0])
        y = float(params[1])

        p = perlin_noise.generate(x, y, freq, hash_table, unit_vectors)
        print('{0}'.format(p))
