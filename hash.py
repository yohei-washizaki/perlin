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
    parser.add_argument("-p", "--perm", type= int, help="permination")
    args = parser.parse_args()

    ht = HashTable(args.hashtable)

    perm = 1
    if args.perm:
        perm = args.perm

    for line in sys.stdin:
        s = line.strip()
        if not s:
            break
        
        v = s.split(' ')
        

        xi = int(v[0]) % perm
        yi = int(v[1]) % perm
        xj = (int(v[0]) + 1) % perm
        yj = (int(v[1]) + 1) % perm
        
        aa = ht.hash(ht.hash(xi) + yi)
        ab = ht.hash(ht.hash(xi) + yj)
        ba = ht.hash(ht.hash(xj) + yi)
        bb = ht.hash(ht.hash(xj) + yj)
        print('{0} {1} {2} {3} {4[2]} {4[3]}'.format(aa, ab, ba, bb, v))
