#!usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from math import floor
from statistics import mean

# noinspection GrazieInspection
# the prompt to help users use this program
_PROMPT = """Calculate the `Combat Speed` of the fleet.

Provide one or two groups of speeds, separate groups with spaces ` ` and numbers with commas `,`.
For example,
    >>> mean 34,39,36 35,36
    35

In this case, `34,39,36` is the first group, and `35,36` is the second. """


def parse_arguments(args: list[str]) -> list[list[float]]:
    """ parse arguments from str to float """
    return [
        [float(x.strip()) for x in arg.split(',') if x.strip()]
        for arg in args if arg.strip()
    ]


def process_one_group(a: list[float]) -> float:
    """ If one group, calculate and print the mean of the group """
    return round(mean(a), 2)


def process_two_groups(a: list[float], b: list[float]) -> float:
    """ If two groups, calculate and print the minimum mean of the two groups """
    return floor(min(mean(a), mean(b)))


def do_calc(argv: list[str]) -> float:
    """ Calculate the mean """
    match len(argv):
        case 1:
            args = parse_arguments(argv)
            return process_one_group(*args)
        case 2:
            args = parse_arguments(argv)
            return process_two_groups(*args)
        case _:
            # If more than two groups, raise an error
            raise TypeError(f'too many arguments, required 0, 1 or 2 but got {len(argv)}: {argv}')


def main() -> None:
    # noinspection GrazieInspection
    """ Calculate the mean of input numbers

    Input arguments can be one or two groups of numbers, and the numbers can be integers or floats.
    Separate groups with spaces ` ` and numbers with commas `,`.

    For example,
        >>> mean 34,39,36 35,36
        35

    In this case, `34,39,36` is the first group, and `35,36` is the second.
    """
    try:
        argv = sys.argv[1:]
        if not argv:
            print(_PROMPT)
            return

        res = do_calc(argv)
        print(res)
    except ValueError as e:
        # exit with code 5: data format error
        print(f'{e.__class__.__name__}: {e}')
        sys.exit(5)
    except TypeError as e:
        # exit with code 2: argument error
        print(f'{e.__class__.__name__}: {e}')
        sys.exit(2)


if __name__ == '__main__':  # pragma: no cover
    main()
