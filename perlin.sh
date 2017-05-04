#!/usr/bin/env bash
SIZE=256
SEED=114514
SCALE=2

RANDOM_TABLE=$(
    for i in `seq 1 2`; do
	./genrndtbl.py $SIZE -s $SEED
    done | sed '$!s/$/ /' | tr -d '\n'
	    )

./uv.py $SIZE | ./scaler.py $SCALE | ./perlin.py | ./hash.py $RANDOM_TABLE
