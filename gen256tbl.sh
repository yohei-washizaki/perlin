#!/usr/bin/env bash
SIZE=256
SEED=114514

for i in `seq 1 2`; do
    ./genrndtbl.py $SIZE -s $SEED
done
# | sed '$!s/$/,/' | tr -d '\n'
