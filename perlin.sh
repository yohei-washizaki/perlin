#!/usr/bin/env bash

PROGNAME=$(basename $0)
VERSION="1.0"
SIZE=256
FREQ=8
SEED=""


usage(){
    echo "usage: $PROGNAME [-h | --help] [-v | --version]"
    echo "                 [-s | --size] [-f | --frequency]"
    echo "                 [-r | --random-seed]"
    echo "                 FILENAME"
    echo
    echo "Generates perline noise texture."
    echo
    echo "options:"
    echo "-h, --help        : show this help and exit."
    echo "-v, --version     : show version info and exit."
    echo "-s, --size        : specify size of generated texture."
    echo "-f, --frequency   : specify frequency."
    echo "-r, --random-seed : specify random seed. If not None is given."
    echo
    exit 1
}


for OPT in "$@"; do
    case "$OPT" in
	'-h'|'--help' )
	    usage
	    exit 1
	    ;;
	'-v'|'--version' )
	    echo $VERSION
	    exit 1
	    ;;
	'-f'|'--frequency' )
	    if [[ -z "$2" ]] || [[ "$2" =~ ^-+ ]]; then
		echo "$PROGNAME: option requires an argument -- $1" 1>&2
		exit 1
	    fi
	    FREQ="$2"
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
	'-s'|'--size' )
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
	-*)
	    echo "$PROGNAME: illegal option -- '$(echo $1 | sed 's/^-*//')'" 1>&2
	    exit 1
	    ;;
	*)
	    if [[ ! -z "$1" ]] && [[ ! "$1" =~ ^-+ ]]; then
		OUTPUT+=( "$1" )
		shift 1
	    fi
	    ;;
    esac
done

if [ -z $OUTPUT ]; then
    usage
    exit 1
fi

RANDOM_TABLE=$(
    for i in `seq 1 2`; do
	./genrndtbl.py $SIZE $SEED
    done | sed '$!s/$/ /' | tr -d '\n'
	    )

# 1.0 0 0.7 0.7 0 1.0 ...
# means
# (1.0 0) (0.7 0.7) (0 1.0) ...
UNIT_VEC=$( ./unitvec.py 8 | sed '$!s/$/ /' | tr -d '\n' )

./uv.py $SIZE | ./scaler.py $FREQ | ./splitfloat.py | ./hash.py -p $FREQ $RANDOM_TABLE | ./perlin.py -u $UNIT_VEC | ./array2image.py $OUTPUT

