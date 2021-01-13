import sys
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide" # avoid hello from pycharm
from picture import Picture
from blob import Blob
from beadfinder import BeadFinder
from glob import glob


def main():
    min_pixels = float(sys.argv[1])
    tau = float(sys.argv[2])
    delta = float(sys.argv[3])
    
    # fix error when we have * in args
    pictures = sys.argv[4:] if len(sys.argv) > 5 else glob(sys.argv[4])

    for i in range(len(pictures)-1):
        beadsOne = BeadFinder(Picture(pictures[i]), tau).getBeads(min_pixels)
        beadsTwo = BeadFinder(Picture(pictures[i+1]), tau).getBeads(min_pixels)

        for beadOne in beadsOne:
            smalllest = float('inf')

            for beadTwo in beadsTwo:
                distance = beadOne.distanceTo(beadTwo)
                if distance < smalllest and distance <= delta: smalllest = distance

            if smalllest <= delta:  print('%.4f' % smalllest)
        
        print()


if __name__ == "__main__":
    main()
    