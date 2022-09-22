#!/usr/bin/env python3

# Created by: Venika Sem
# Created on: Sept 2020
# This program calculates the area and perimeter of a circle
#    with radius 15mm

import math


def main():
    # this function calculates the area and perimeter

    print("The radius of a circle is 15 mm: ")
    print("")
    print("Then the area is {} mm².".format(math.pi * 15**2))
    print("Then the perimeter is {} mm.".format(2 * math.pi * 15))
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
