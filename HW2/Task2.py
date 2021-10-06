#2.Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).


def test():
    assert digit('576342') == f'\nчетные цифры: 6, 4, 2; кол: 3\nнечетные цифры: 5, 7, 3; кол: 3', 'incorrect'
    assert digit('11342') == f'\nчетные цифры: 4, 2; кол: 2\nнечетные цифры: 1, 1, 3; кол: 3', 'incorrect'
    assert digit('-342') == f'\nОШИБКА: Введите только натуральное число:', 'incorrect'
    assert digit('sfs') == f'\nОШИБКА: Введите только натуральное число:', 'incorrect'

    print('Test: OK')


def digit(value):
    global l_num
    l_num = []
    try:
        value = int(value)
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
        return f'\nчетные цифры: {", ".join(even_num) if even_num!=[] else "нет"}; кол: {len(even_num)}\nнечетные цифры: {", ".join(odd_num) if odd_num!=[] else "нет"}; кол: {len(odd_num)}'
    return
  


test()
while l_num==[]:
    print(digit(input('\nВведите натуральное число:\n')))

