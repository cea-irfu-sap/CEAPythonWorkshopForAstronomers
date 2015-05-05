"""Simple program to convert between distance units"""

from __future__ import print_function

# As a convention, we import the standard modules first
import argparse
import sys

# Then, we import the user-defined modules
import conversions

def format_precision(precision, value):
    """Format a value with the given number of digits in scientific notation"""
    p = precision - 1 # the format descriptions takes the number of digits after the point
    format_str = "{{:.{}e}}".format(p) # the format string is something like "{:.3e}"
    return format_str.format(value)

if __name__ == '__main__':
    # Set up the argument parser
    parser = argparse.ArgumentParser(description=__doc__)
    # __doc__ is a shortcut to the current module's docstring

    # Regroup conversion options
    parser.add_argument("value", type=float, help="value to convert")
    parser.add_argument("-f", "--from", type=str, help="source unit", required=True, dest="from_", metavar="FROM_UNIT")
    # we put the source unit into "from_" because "from" is a reserved word
    parser.add_argument("-t", "--to", type=str, help="destination unit", required=True, metavar="TO_UNIT")
    parser.add_argument("-p", "--precision", type=int, help="number of significant digits")

    # Parse the command-line options
    args = parser.parse_args()

    # Print an error message and exit in case of unknown units
    if args.from_ not in conversions.DISTANCE_UNITS:
        parser.error("unknown unit '{}'".format(args.from_))
    if args.to not in conversions.DISTANCE_UNITS:
        parser.error("unknown unit '{}'".format(args.to))

    # Print an error message and exit when the precision is less than 1
    if args.precision is not None and args.precision < 1:
        parser.error("precision should be at least 1")

    # Perform the conversion
    result = conversions.convert_distance(args.value, args.from_, args.to)

    # Format the result
    if args.precision is None:
        result = str(result)
    else:
        result = format_precision(args.precision, result)

    # Output the result
    print(result)

