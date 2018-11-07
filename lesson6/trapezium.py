import math
class Trapezium():
    def __init__(self, ls):
        self._xa = ls[0][0]
        self._ya = ls[0][1]
        self._xb = ls[1][0]
        self._yb = ls[1][1]
        self._xc = ls[2][0]
        self._yc = ls[2][1]
        self._xd = ls[3][0]
        self._yd = ls[3][1]
        self._ab = math.sqrt((self._xb - self._xa)**2 + (self._yb - self._ya)**2)
        self._bc = math.sqrt((self._xc - self._xb)**2 + (self._yc - self._yb)**2)
        self._cd = math.sqrt((self._xd - self._xc)**2 + (self._yd - self._yc)**2)
        self._da = math.sqrt((self._xa - self._xd)**2 + (self._ya - self._yd)**2)
        self._ac = math.sqrt((self._xc - self._xa)**2 + (self._yc - self._ya)**2)
        self._bd = math.sqrt((self._xd - self._xb)**2 + (self._yd - self._yb)**2)


    def is_trapezium_equipolar(self):
        return True if self._ac == self._bd else False


    def len_line(self):
        return self._ab, self._bc, self._cd, self._da


    def square(self):
        return (self._da + self._ab) / 2*math.sqrt(self._bc**2 - ((self._ab - self._da)**2 + self._bc**2 - self._cd**2) / 2*(self._ab - self._da))

    def perimetr(self):
        return self._ab + self._bc + self._cd + self._da


if __name__== '__main__':
    trapezium = Trapezium([[1,1],[2,3],[4,3],[5,1]])
    print('Is trapezium ravn ',trapezium.is_trapezium_equipolar())
    print('Square is = ',trapezium.square())
    a,b,c,d = trapezium.len_line()
    print('Lens is a={} b={} c={} d={}'.format(a,b,c,d))
