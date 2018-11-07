from rectangle import Rectangle
from trapezium import Trapezium



if __name__ == '__main__':
    print('Треугольник')
    rectangle = Rectangle(1, 9, 4, 3, 5, 7)
    print('Площадь треугольника = ', rectangle.square())
    print('Высота = ', rectangle.higth())
    print('Периметр = ', rectangle.perimetr())


    print('Trapezuim')
    trapezium = Trapezium([[1, 1], [2, 3], [4, 3], [5, 1]])
    print('Трапеция равнобочная? ', trapezium.is_trapezium_equipolar())
    print('Площадь трапеции = ', trapezium.square())
    a, b, c, d = trapezium.len_line()
    print('Длины сторон трапеции a={} b={} c={} d={}'.format(a, b, c, d))
    print('Периметр трапеции =',trapezium.perimetr())

