# 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.

# Блок-схема- алгоритм (открывать в google chrome)
# https://www.figma.com/file/a0iyIqDMX5BU21Itfgwya3/HW3-Task8?node-id=0%3A1

res=[]

def test():
    assert matrix(
        [[8, 3, 15, 6, 32], [3, 4, 3, 2, 12], [5, 6, 7, 8, 26],
         [9, 8, 6, 4, 27]]
    ) == f'\nМатрица:\n8 3 15 6 32 \n3 4 3 2 12 \n5 6 7 8 26 \n9 8 6 4 27 \n', 'incorrect'
    assert matrix(
        [[8, 3, 15, 6, 32], [3, 4, 3, 2], [5, 6, 7, 8],
         [9, 8, 6, 4, 27]]
    ) == f'\nОШИБКА: кол-во колонок в строках не равны', 'incorrect'
    assert matrix(
        [[8, 3, 's', 3], [3, 'g', 4, 1], [5, 6, 'f', 1], ['d', 8, 1, 6]]
    ) == f'\nОШИБКА: в матрице должны быть только цифры', 'incorrect'
    assert matrix(
        [[' '], [' '], [' '], [' ']]
    ) == f'\nОШИБКА: в матрице должны быть только цифры', 'incorrect'
    print('Test: OK\n')

    




def calculate(_row):
    res = []
    for _n in range(1, _row + 1):
        try:
            _line = list(map(int, input(f'Строка {_n}:\n').split(' ')))
            if len(_line) != 4:
                raise ValueError
            else:
                _line.append(sum(_line))
                res.append(_line)
        except ValueError or TypeError:
            return f'\nОШИБКА: необходимо ввести 4 цифры для строки (через пробел)'
    return res


def matrix(arr):
    _matrix = ''
    if type(arr)==list:
        _head=len(arr[0])
        for _col in range(1, len(arr)):
            if _head!=len(arr[_col]):
                return f'\nОШИБКА: кол-во колонок в строках не равны'

        for _i in range(len(arr)):
            _row = ''
            for _j in range(len(arr[_i])):
                try:
                    int(arr[_i][_j])
                    _row += f'{arr[_i][_j]} '
                except ValueError or TypeError:
                    return f'\nОШИБКА: в матрице должны быть только цифры'
            _matrix += f'{_row}\n'
        arr=f'\nМатрица:\n{_matrix}'
    return arr

test()
print(matrix(calculate(4)))
