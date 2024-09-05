#!/usr/bin/python3

import sys

if len(sys.argv) > 2:
    print("{} arguments:" .format(len(sys.argv) - 1))
elif len(sys.argv) == 2:
    print("{} argument:" .format(len(sys.argv) - 1))
    j = 1
    for argument in sys.argv[1:]:
        print("{}: {}" .format(j, argument))
        j += 1
elif len(sys.argv) == 1:
    print("0 arguments.")
