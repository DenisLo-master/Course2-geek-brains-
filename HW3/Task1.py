#1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.


def test():
    assert multiple_digit(
        2, 10
    ) == f'Диапазон 2:9\n\nКол. чисел кратно 2: 4\nКол. чисел кратно 3: 3\nКол. чисел кратно 4: 2\nКол. чисел кратно 5: 1\nКол. чисел кратно 6: 1\nКол. чисел кратно 7: 1\nКол. чисел кратно 8: 1\nКол. чисел кратно 9: 1', 'incorrect'
    assert multiple_digit(
        -342,'f'
    ) == f'\nОШИБКА: необходимо передать только диапазон чисел', 'incorrect'
    assert multiple_digit(
        'sfs',100
    ) == f'\nОШИБКА: необходимо передать только диапазон чисел', 'incorrect'
    assert multiple_digit(
        0,0
    ) == f'\nОШИБКА: необходимо передать только диапазон чисел', 'incorrect'
    assert multiple_digit(
        '',''
    ) == f'\nОШИБКА: необходимо передать только диапазон чисел', 'incorrect'
    assert multiple_digit(
        ' ',' '
    ) == f'\nОШИБКА: необходимо передать только диапазон чисел', 'incorrect'
    print('Test: OK\n')


def multiple_digit(value1, value2):
    try:
        value = range(value1, value2)
        if value1==value2:
          raise TypeError
        res = []
        for _i in range(2, 10):
            list_mult = []
            for _num in value:
                if _num % _i == 0:
                    list_mult.append(_num)
            res.append(f'Кол. чисел кратно {_i}: {len(list_mult)}')
        return f'Диапазон {value1}:{value2-1}\n\n' + '\n'.join(res)
    except TypeError:
        return f'\nОШИБКА: необходимо передать только диапазон чисел'


test()
value1 = 2
value2 = 100

print(multiple_digit(value1, value2))
