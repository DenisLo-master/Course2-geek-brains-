#9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.


def test():
    assert calculate(
        '1245 123 298 2353 223') == f'Число: 298, макс. сумма 19', 'incorrect'
    assert calculate(
        '6245 523 018 2343 293') == f'Число: 6245, макс. сумма 17', 'incorrect'
    assert calculate('1234') == f'Число: 1234, макс. сумма 10', 'incorrect'
    assert calculate('-1234') == f'\nОШИБКА: Введите числа', 'incorrect'
    assert calculate('ff') == f'\nОШИБКА: Введите числа', 'incorrect'
    assert calculate(' ') == f'\nОШИБКА: Введите числа', 'incorrect'
    assert calculate('') == f'\nОШИБКА: Введите числа', 'incorrect'
    print('Test: OK\n')


def calculate(value):
    num_dict={}
    sum_list=[]
    try:
        value=list(map(int, value.split(' ')))
        for l in value:
            sum_l = 0
            for s in str(l):
                sum_l += int(s)
            sum_list.append(sum_l)
            num_dict[sum_l]=l
        sum_list.sort()
        max_sum=sum_list[-1]
        return f'Число: {num_dict[max_sum]}, макс. сумма {max_sum}'
    except ValueError:
        return f'\nОШИБКА: Введите числа'


test()
print(calculate(input('Введите числа через пробел:\n')))
