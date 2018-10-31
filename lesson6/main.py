from rectangle import Rectangle
from trapezium import Trapezium



if __name__ == '__main__':
    print('Rectangle')
    rectangle = Rectangle(1, 9, 4, 3, 5, 7)
    print('Square = ', rectangle.square())
    print('Higth = ', rectangle.higth())
    print('Perimatr = ', rectangle.perimetr())


    print('Trapezuim')
    trapezium = Trapezium([[1, 1], [2, 3], [4, 3], [5, 1]])
    print('Is trapezium ravn ', trapezium.is_trapezium_ravn())
    print('Square is = ', trapezium.square())
    a, b, c, d = trapezium.len_line()
    print('Lens is a={} b={} c={} d={}'.format(a, b, c, d))

