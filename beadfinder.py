import sys, stddraw
from color import Color
from picture import Picture
from blob import Blob

white = Color(255, 255, 255)
black = Color(0, 0, 0)

def luminance(c):
    red = c.getRed()
    green = c.getGreen()
    blue = c.getBlue()
    return (.299 * red) + (.587 * green) + (.114 * blue)


class BeadFinder:
    def __init__(self, picture, tau):
        """
        Constructs a blob finder to find blobs in the picture pic, using
        a luminance threshold tau.        
        """

        self._picture = picture
        # create a set with picture size
        self._temp = [[False]*self._picture.width() for item in range(self._picture.height())]
        self._beads = []

        for row in range(self._picture.height()):
            for col in range(self._picture.width()):
                pixel = self._picture.get(col, row)
                Y = luminance(pixel)
                if Y >= tau :
                    self._temp[row][col] = True

        for row in range(self._picture.height()):
            for col in range(self._picture.width()):
                if self._temp[row] [col]:
                    blob = Blob()
                    self.__proccess(blob, self._temp, row, col)
                    self._beads.append(blob)


    def getBeads(self, min_pixels):
        """
        Returns a list of all beads at least with min_pixels pixels.
        """

        return [item for item in self._beads if item.mass() >= min_pixels]


    def __proccess(self, blob, array, i=0, j=0):
        if not array[i][j] : return

        # mark the pixel if it is white
        blob.add(i, j)
        array[i][j] = False

        # try catch for prvent index out of range
        try: self.__proccess(blob, array, i+1, j) # Up
        except: pass 
        try: self.__proccess(blob, array, i, j+1) # Right
        except: pass 
        try: self.__proccess(blob, array, i-1, j) # Down
        except: pass 
        try: self.__proccess(blob, array, i, j-1) # left
        except: pass 


def main():
    # for test this class
    x = BeadFinder(Picture(sys.argv[3]), float(sys.argv[2]))
    for item in x.getBeads(int(sys.argv[1])): print(str(item))


if __name__ == "__main__":
    main()