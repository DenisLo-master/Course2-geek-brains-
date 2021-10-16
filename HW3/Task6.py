# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.

# Блок-схема- алгоритм (открывать в google chrome)
# https://www.figma.com/file/O2kjffn4ZUP4fR3Qcs2UmO/HW3-Task6?node-id=0%3A1


def test():
    assert sum_between(
        [8, 3, 15, 6, 4, 2]
    ) == f'Список: [8, 3, 15, 6, 4, 2]\nСумма между min(2) и max(15): 21', 'incorrect'
    assert sum_between(
        ['8', '3', '15', '6', '4', '2']
    ) == f'Список: [8, 3, 15, 6, 4, 2]\nСумма между min(2) и max(15): 21', 'incorrect'
    assert sum_between(
        ['8', '3', '6', '6', '3', '15']
    ) == f'Список: [8, 3, 6, 6, 3, 15]\nСумма между min(3) и max(15): 20', 'incorrect'
    assert sum_between([
        -342, 'f'
    ]) == f'\nОШИБКА: необходимо передать только массив чисел', 'incorrect'
    assert sum_between([
        'sfs', 100
    ]) == f'\nОШИБКА: необходимо передать только массив чисел', 'incorrect'
    assert sum_between([
        '', ''
    ]) == f'\nОШИБКА: необходимо передать только массив чисел', 'incorrect'
    assert sum_between([
        ' ', ' '
    ]) == f'\nОШИБКА: необходимо передать только массив чисел', 'incorrect'
    print('Test: OK\n')


def sum_between(list1):
    try:
        list1 = list(map(int, list1))
        _list = list1.copy()
        _list.sort()
        min = list1.index(_list[0])
        max = list1.index(_list[-1])
        res = 0
        for _num in range(len(_list)):
            if _list[_num] == list1[min] or _list[_num] == list1[max]:
                _list[_num]=0
            else:
                res += _list[_num]
        return f'Список: {list1}\nСумма между min({list1[min]}) и max({list1[max]}): {res}'
    except ValueError or TypeError:
        return f'\nОШИБКА: необходимо передать только массив чисел'


test()

list1 = [7, 3, 3, 6, 6, 4]
print(sum_between(list1))
