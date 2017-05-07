#!/usr/bin/env python3
import genrndtbl


class HashTable:
    def __init__(self, table):
        self.table = table
        self.size = len(table)

    def hash(self, x):
        return self.table[x % self.size]

    @staticmethod
    def Create(length, seed=None):
        t = genrndtbl.generate_random_table(length, seed)
        return HashTable(t)


if __name__ == "__main__":
    import sys
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--length", type=int,
                        default=256, help="length of table")
    parser.add_argument("-r", "--random_seed", type=int, help="random seed")
    args = parser.parse_args()

    ht = HashTable.Create(args.length, args.random_seed)

    for line in sys.stdin:
        s = line.strip()
        if not s:
            break

        v = s.split(' ')

        xi = int(v[0])
        yi = int(v[1])
        xj = (int(v[0]) + 1)
        yj = (int(v[1]) + 1)

        aa = ht.hash(ht.hash(xi) + yi)
        ab = ht.hash(ht.hash(xi) + yj)
        ba = ht.hash(ht.hash(xj) + yi)
        bb = ht.hash(ht.hash(xj) + yj)
        print('{0} {1} {2} {3} {4[2]} {4[3]}'.format(aa, ab, ba, bb, v))
