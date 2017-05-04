#!/usr/bin/env bash

OUTPUT=$1
SIZE=256
SEED="-s 2"
SCALE=3
RANDOM_TABLE=$(
    for i in `seq 1 2`; do
	./genrndtbl.py $SIZE $SEED
    done | sed '$!s/$/ /' | tr -d '\n'
	    )

./uv.py $SIZE | ./scaler.py $SCALE | ./splitfloat.py | ./hash.py $RANDOM_TABLE | ./perlin.py | ./array2png.py $OUTPUT
#./uv.py $SIZE | ./scaler.py $SCALE | ./splitfloat.py | ./hash.py $RANDOM_TABLE | ./perlin.py
