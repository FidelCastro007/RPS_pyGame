# import math
from math import pi # it only imports pi from math module
import random as rdm #aliases

print(pi)
#print(dir(rdm))

for item in dir(rdm):
    print(item)

#import User_Input
import challenges.rps8 as rps8

print(__name__)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience."
    )

    parser.add_argument(
        '-n', '--name', metavar='name',
        required=True, help='The name of the person playing the game.'
    )

    args = parser.parse_args()
    rps8.rps(args.name)