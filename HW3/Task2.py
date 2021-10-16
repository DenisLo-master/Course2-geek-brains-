#2. Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.

# Блок-схема- алгоритм (открывать в google chrome) 
# https://www.figma.com/file/lbVTlD2l4XFiDwB8a4dEXb/HW3-Task2?node-id=0%3A1

def test():
    assert index_even(
        [8, 3, 15, 6, 4, 2]
    ) == f'Список: [8, 3, 15, 6, 4, 2]\nИндексы четных чисел из list1:[0, 3, 4, 5]', 'incorrect'
    assert index_even(
        ['8', '3', '15', '6', '4', '2']
    ) == f'Список: [8, 3, 15, 6, 4, 2]\nИндексы четных чисел из list1:[0, 3, 4, 5]', 'incorrect'
    assert index_even([
        -342, 'f'
    ]) == f'\nОШИБКА: необходимо передать только список чисел', 'incorrect'
    assert index_even([
        'sfs', 100
    ]) == f'\nОШИБКА: необходимо передать только список чисел', 'incorrect'
    assert index_even([
        '', ''
    ]) == f'\nОШИБКА: необходимо передать только список чисел', 'incorrect'
    assert index_even([
        ' ', ' '
    ]) == f'\nОШИБКА: необходимо передать только список чисел', 'incorrect'
    print('Test: OK\n')


def index_even(list1):
    try:
        list1 = list(map(int, list1))
        list2 = []
        for _num in range(len(list1)):
            if list1[_num] % 2 == 0:
                list2.append(_num)
        return f'Список: {list1}\nИндексы четных чисел из list1:{list2}'
    except ValueError or TypeError:
        return f'\nОШИБКА: необходимо передать только список чисел'


test()

list1 = [7, 5, 3, 5, 4, 6, 7, 8, 4]
print(index_even(list1))
