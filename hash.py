#!/usr/bin/env python3


class HashTable:
    def __init__(self, table):
        self.table = table

    def hash(self, x):
        return self.table[x]


if __name__ == "__main__":
    import sys
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("hashtable", type=int, nargs='+', help="table values")
    args = parser.parse_args()

    ht = HashTable(args.hashtable)

    for line in sys.stdin:
        s = line.strip()
        v = s.split(' ')
        # print('{0[0]} {0[1]} {0[2]} {0[3]}'.format(v))
        xi = int(v[0])
        yi = int(v[1])
        aa = ht.hash(ht.hash(xi) + yi) & 0x7
        ab = ht.hash(ht.hash(xi) + yi + 1) & 0x7
        ba = ht.hash(ht.hash(xi + 1) + yi) & 0x7
        bb = ht.hash(ht.hash(xi + 1) + yi + 1) & 0x7
        print('{0} {1} {2} {3} {4[2]} {4[3]}'.format(aa, ab, ba, bb, v))
