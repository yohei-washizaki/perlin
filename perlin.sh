#!/usr/bin/env bash

PROGNAME=$(basename $0)
VERSION="1.0"
SIZE=256
SCALE=2
SEED=""

usage(){
    echo "Usage: $PROGNAME [-h | --help] [-v | --version] [--size] [--scale] [-r | --random-seed] FILENAME"
    echo "Generates perline noise texture."
    echo
    echo "Options:"
    echo "-h, --help        : Show this message."
    echo "-v, --version     : Show version of this script."
    echo "    --size        : Size of generated texture."
    echo "    --scale       : Scale factor for uv coord extension."
    echo "-r, --random-seed : Set random seed. If not system clock is used."
    echo
    exit 1
}

for OPT in "$@"; do
    echo "$@"
    case "$OPT" in
	'-h'|'--help' )
	    usage
	    exit 1
	    ;;
	'-v'|'--version' )
	    echo $VERSION
	    exit 1
	    ;;
	'--scale' )
	    if [[ -z "$2" ]] || [[ "$2" =~ ^-+ ]]; then
		echo "$PROGNAME: option requires an argument -- $1" 1>&2
		exit 1
	    fi
	    SCALE="$2"
	    shift 2
	    ;;
	'-r'|'--random-seed' )
	    if [[ -z "$2" ]] || [[ "$2" =~ ^-+ ]]; then
		echo "$PROGNAME: option requires an argument -- $1" 1>&2
		exit 1
	    fi
	    SEED=("-s $2")
	    shift 2
	    ;;
	'--size' )
	    if [[ -z "$2" ]] || [[ "$2" =~ ^-+ ]]; then
		echo "$PROGNAME: option requires an argument -- $1" 1>&2
		exit 1
	    fi
	    SIZE=("$2")
	    shift 2
	    ;;
	'--'|'-' )
	    shift 1
	    OUTPUT+=( "$@" )
	    break
	    ;;
	*)
	    if [[ ! -z "$1" ]] && [[ ! "$1" =~ ^-+ ]]; then
		OUTPUT+=( "$1" )
		shift 1
	    fi
	    ;;
    esac
done

echo "size:   $SIZE"
echo "scale:  $SCALE"
echo "output: $OUTPUT"
echo "seed:   $SEED"

RANDOM_TABLE=$(
    for i in `seq 1 2`; do
	./genrndtbl.py $SIZE $SEED
    done | sed '$!s/$/ /' | tr -d '\n'
	    )

./uv.py $SIZE | ./scaler.py $SCALE | ./splitfloat.py | ./hash.py $RANDOM_TABLE | ./perlin.py | ./array2png.py $OUTPUT
