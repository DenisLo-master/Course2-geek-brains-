#1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа. Числа и знак операции вводятся пользователем. После выполнения вычисления программа не должна завершаться, а должна запрашивать новые данные для вычислений. Завершение программы должно выполняться при вводе символа '0' в качестве знака операции. Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и снова запрашивать знак операции. Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.

# Блок-схема- алгоритм (открывать в google chrome) https://www.figma.com/file/IDqU18bTZyUfrze1cELTJU/HW2-Task1?node-id=0%3A1

d1 = None
d2 = None
sing_oprn = str


def test():
    assert calculation(5, 7, '+') == 12, 'incorrect'
    assert calculation(5, 0, '+') == 5, 'incorrect'
    assert calculation(1, 7, '-') == -6, 'incorrect'
    assert calculation(15, 8, '-') == 7, 'incorrect'
    assert calculation(0, 7, '*') == 0, 'incorrect'
    assert calculation(5, 7, '*') == 35, 'incorrect'
    assert calculation(15, 3, '/') == 5, 'incorrect'
    assert 2.857 <= calculation(20, 7, '/') <= 2.858, 'incorrect'
    assert calculation(3, 0, '/')==f'Деление на 0 невозможно\n', 'incorrect'
    print(f'Test: OK\n')


def digit(value):
    global d1, d2
    try:
        value = float(value)
        if d1 == None:
            d1 = value
            operation(input('\nВведите тип операции, либо "0" для выхода: \n'))
        else:
            d2 = value
            print(f'\nРешение: {calculation(d1, d2, sign_oprn)}')
            d1, d2 = None, None
            return
    except ValueError:
        digit(input('\nОШИБКА: Введите только число: \n'))


def operation(value):
    global sign_oprn
    if value == '0':
        exit()
    elif value in ['+', '-', '*', '/']:
        sign_oprn = value
        digit(input('\nВведите второе число: \n'))
    else:
        operation(
            input(
                '\nОШИБКА: введите только тип операции, либо "0" для выхода: \n'
            ))


def calculation(d1, d2, sign_oprn):

    if sign_oprn == '+':
        return d1 + d2
    if sign_oprn == '-':
        return d1 - d2
    if sign_oprn == '*':
        return d1 * d2
    if sign_oprn == '/':
        try:
            return d1 / d2
        except ZeroDivisionError:
            return f'Деление на 0 невозможно\n'


test()

while True:
    digit(input('\n-------\nВведите первое число: \n'))
