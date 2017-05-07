#!/usr/bin/env python3
import math


class UnitVectors:
    """List of unit vectors"""
    def __init__(self, vectors):
        self.vectors = vectors

    def __getitem__(self, k):
        return self.vectors[k % len(self.vectors)]

    @staticmethod
    def Create(count=8):
        step = 360.0 / count
        unit_vectors = []
        for i in range(count):
            radian = math.radians(i * step)
            unit_vectors.append((math.cos(radian), math.sin(radian)))

        return UnitVectors(unit_vectors)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("count", type=int, help="count of created vectors.")
    args = parser.parse_args()

    unit_vectors = UnitVectors.Create()

    for v in unit_vectors:
        print('{0[0]:.16f} {0[1]:.16f}'.format(v))
