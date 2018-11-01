import math
class Rectangle():
    def __init__(self,xa,ya,xb,yb,xc,yc):
        self._xa = xa
        self._ya = ya
        self._xb = xb
        self._yb = yb
        self._xc = xc
        self._yc = yc
        self._a = math.sqrt((self._xb - self._xa)**2 + (self._yb - self._ya)**2)
        self._b = math.sqrt((self._xc - self._xb)**2 + (self._yc - self._yb)**2)
        self._c = math.sqrt((self._xc - self._xa)**2 + (self._yc - self._ya)**2)
        self._p = (self._a + self._b + self._c) / 2

    def square(self):
        return math.sqrt(self._p * (self._p - self._a) * (self._p - self._b) * (self._p - self._c))

    def higth(self):
        return 2 * math.sqrt(self._p * (self._p - self._a) * (self._p - self._b) * (self._p - self._c)) / self._a

    def perimetr(self):
        return self._a + self._b + self._c


if __name__ == '__main__':
    rectangle = Rectangle(1,9,4,3,5,7)
    print('Square = ',rectangle.square())
    print('Higth = ',rectangle.higth())
    print('Perimatr = ',rectangle.perimetr())