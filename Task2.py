#2.Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

# Блок-схема- алгоритм (открывать в google chrome)  https://www.figma.com/file/aSypyNeKcYtLCKPvl7ycwv/HW2-Task2?node-id=0%3A1

l_num = []


def test():
    assert digit(
        '576342'
    ) == f'\n3 четные цифры (6, 4 и 2)\n3 нечетные цифры (5, 7 и 3)', 'incorrect'
    assert digit(
        '11342'
    ) == f'\n2 четные цифры (4 и 2)\n3 нечетные цифры (1, 1 и 3)', 'incorrect'
    assert digit(
        '-342') == f'\nОШИБКА: Введите только натуральное число:', 'incorrect'
    assert digit(
        'sfs') == f'\nОШИБКА: Введите только натуральное число:', 'incorrect'
    assert digit(
        '0') == f'\nОШИБКА: Введите только натуральное число:', 'incorrect'

    print('Test: OK')


def digit(value):
    global l_num
    l_num = []
    try:
        value = int(value)
        if value == 0:
            raise ValueError
        value = str(value)
        for i in value:
            l_num.append(i)
        return calculation(l_num)
    except ValueError:
        return f'\nОШИБКА: Введите только натуральное число:'


def calculation(l_num):
    even_num = []
    odd_num = []
    if l_num != []:
        for i in l_num:
            if int(i) % 2 == 0:
                even_num.append(i)
            else:
                odd_num.append(i)
        count_e_num = len(even_num)
        if even_num != []:
            e_num = f'({", ".join(even_num[0:-1])} и {even_num[-1]})'
        else:
            e_num = '- отсутсвтуют'
        count_o_num = len(odd_num)
        if odd_num != []:
            o_num = f'({", ".join(odd_num[0:-1])} и {odd_num[-1]})'
        else:
            o_num = '- отсутсвтуют'
        return f'\n{count_e_num if count_e_num!=0 else ""} четные цифры {e_num}\n{count_o_num if count_o_num!=0 else ""} нечетные цифры {o_num}'
    return


test()
while l_num == []:
    print(digit(input('\nВведите натуральное число:\n')))
