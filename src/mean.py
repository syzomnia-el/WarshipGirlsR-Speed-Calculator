#!usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from math import floor
from statistics import mean

# the prompt to help users use this program
_PROMPT = """Calculate the `Combat Speed` of the fleet.

Provide one or two groups of speeds, separate groups with spaces ` ` and numbers with commas `,`.
For example,
    >>> mean 34,39,36 35,36
    35

In this case, `34,39,36` is the first group, and `35,36` is the second. """


def parse_arguments(args: list[str]) -> list[list[float]]:
    return [
        [float(x.strip()) for x in arg.split(',') if x.strip()]
        for arg in args if arg.strip()
    ]


def main() -> None:
    # noinspection PyUnresolvedReferences
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
        args = parse_arguments(argv)
        match len(argv):
            case 0:
                # If no argument, print the prompt
                print(_PROMPT)
            case 1:
                # If one group, calculate and print the mean of the group
                avg = mean(args[0])
                print(f'{avg:.2f}')
            case 2:
                # If two groups, calculate and print the minimum mean of the two groups
                avg1 = mean(args[0])
                avg2 = mean(args[1])
                print(floor(min(avg1, avg2)))
            case _:
                # If more than two groups, raise an error
                raise TypeError(f'too many arguments, required 0, 1 or 2 but got {len(argv)}: {argv}')
    except ValueError as e:
        # exit with code 5: data format error
        print(f'{e.__class__.__name__}: {e}')
        sys.exit(5)
    except TypeError as e:
        # exit with code 2: argument error
        print(f'{e.__class__.__name__}: {e}')
        sys.exit(2)


if __name__ == '__main__':
    main()  # pragma: no cover
