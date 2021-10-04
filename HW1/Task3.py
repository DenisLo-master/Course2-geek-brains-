#3. По введенным пользователем координатам двух точек вывести уравнение прямой вида y=kx+b, проходящей через эти точки.


def equation(x1, y1, x2, y2):
    try:
        if x1 == x2:
            raise ZeroDivisionError
        k = (y1 - y2) / (x1 - x2)
        b = y2 - k * x2
        return k, b
    except ZeroDivisionError:
        print('\nОШИБКА деления на 0: значения x1 и x2 совпадают')
        exit()


def test():
    assert equation(4, 2, 3, 2) == (0, 2), 'incorrect'
    assert (0.8, -2.2) <= equation(9, 5, 4, 1) <= (0.81, -2.21), 'incorrect'
    assert (0.625, 1.375) <= equation(1, 2, 9,
                                      7) <= (0.626, 1.376), 'incorrect'
    assert equation(1, 10, 2, 12) == (2, 8), 'incorrect'

    #assert equation(1, 10, 1, 12) == False, 'incorrect'

    print('Test: OK\n')


test()

try:
    x1, y1 = map(float,
                 input('Введите координаты ПЕРВОЙ точки (x;y): ').split(';'))
except ValueError:
    print('\nОШИБКА: Вводите х и y координаты, в формате ’x;y’')
    exit()

try:
    x2, y2 = map(float,
                 input('\nВведите координаты ВТОРОЙ точки (x;y): ').split(';'))

except ValueError:
    print('\nОШИБКА: Вводите х и y координаты, в формате ’x;y’')
    exit()

k, b = equation(x1, y1, x2, y2)

if b > 0:
    print(f'\nУравнение: y = {k} * x +{b}')
else:
    print(f'\nУравнение: y = {k} * x {b}')
