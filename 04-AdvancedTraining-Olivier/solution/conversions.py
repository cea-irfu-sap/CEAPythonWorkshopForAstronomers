"""Make conversions between units"""

from __future__ import print_function

import math
import scipy.constants as const

# Calculate the value of a parsec in meters
PARSEC = const.astronomical_unit / math.tan(math.radians(1. / 3600.))

DISTANCE_UNITS = { # key: unit name, value: unit value in m
    'cm': 0.01,
     'm': 1.0,
    'km': 1000.0,
    'au': const.astronomical_unit,
    'ly': const.c * const.year,
    'pc': PARSEC,
    'kpc': 1000.0 * PARSEC,
    'Mpc': 1e6 * PARSEC,
    'Gpc': 1e9 * PARSEC
}

def convert_distance(value, from_unit, to_unit):
    """Convert a distance between two given units

    Parameters:
        value     -- float, value of the distance
        from_unit -- string, source unit name
        to_unit   -- string, destination unit name

    Returns:
        value_converted -- float, converted value

    The supported units and their values are stored in the DISTANCE_UNITS dict.
    """
    return value * DISTANCE_UNITS[from_unit] / DISTANCE_UNITS[to_unit]

if __name__ == '__main__':
    print("Forward conversions")
    print("1 m")
    for unit in DISTANCE_UNITS:
        print(" = {} {}".format(convert_distance(1.0, 'm', unit), unit))

    print()
    print("Backward conversions")
    for unit in DISTANCE_UNITS:
        print("1 {:3s} = {} m".format(unit, convert_distance(1.0, unit, 'm')))

