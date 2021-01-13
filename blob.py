import math

class Blob:
    def __init__(self):
        """
        Construct an empty blob.
        """

        self._pixels = []
        self._height = []
        self._width = []

    def __center(self):
        """
        Get center of blob
        """

        x = sum(self._width) / len(self._width)
        y = sum(self._height) / len(self._height)
        return (x, y)

    def add(self, x, y):
        """
        add pixel with x,y position to blob.
        """

        self._pixels.append((x, y))
        self._height.append(y)
        self._width.append(x)

    def mass(self):
        """
        get count of pixels.
        """

        return len(self._pixels)

    def distanceTo(self, c):
        """ 
        get distance from current blob to blob c
        """

        Xc, Yc = c._Blob__center()
        X, Y = self._Blob__center()
        return math.sqrt((X - Xc)**2 + (Y - Yc)**2)

    def __str__(self):
        """
        string representation of this blob.
        """

        x, y = self._Blob__center()
        return ('%d (%.4f, %.4f)' % (self.mass(), y, x))


if __name__ == "__main__":
    # test this class
    b = Blob()
    b.add(4,5)
    c = Blob()
    c.add(100,50)
    print('b : ', b, 'c', c)
    print(c.distanceTo(b))