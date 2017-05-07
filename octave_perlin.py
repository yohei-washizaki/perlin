#!/usr/bin/env python3
from perlin import PerlinNoise
from unitvec import UnitVectors
from hash import HashTable


if __name__ == "__main__":
    import sys
    import argparse

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
    parser.add_argument("-o", "--octaves",
                        type=int, default=8,
                        help="octaves")
    parser.add_argument("-p", "--persistence",
                        type=float, default=1.0,
                        help="persistence")
    args = parser.parse_args()

    unit_vectors = UnitVectors.Create(args.num_vectors)
    hash_table = HashTable.Create(args.hashtable_length, args.random_seed)
    perlin_noise = PerlinNoise()
    default_freq = args.frequency
    octaves = args.octaves
    persistence = args.persistence

    for line in sys.stdin:
        params = line.strip().split(' ')
        x = float(params[0])
        y = float(params[1])

        amplitude = 1.0
        total = 0
        max_value = 0
        frequency = default_freq

        for o in range(octaves):
            total += perlin_noise.generate(x * frequency,
                                           y * frequency,
                                           frequency, hash_table, unit_vectors)
            max_value += amplitude
            amplitude *= persistence
            frequency *= 2

        final_value = total / max_value

        print('{0}'.format(final_value))
