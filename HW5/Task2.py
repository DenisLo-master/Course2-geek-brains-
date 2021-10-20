#2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив, элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
import collections
from collections import deque
import numpy as np

hex = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']
k = 0
j = 0
index_l1 = -1
index_l2 = -1
sum_num = collections.deque()
mul = collections.deque()
res_line = collections.deque()
res_matrix = np.zeros((1, 1))
result = collections.deque()
res = []


def test():
    result.clear()
    assert sum_matrix(np.array([['1', '2'], ['3', '4']]),
                      1) == deque(['4', '6']), 'incorrect'
    result.clear()
    assert sum_matrix(np.array([['E', 'F', '4'], ['2', 'D', 'E']]),
                      2) == deque(['1', '1', 'D', '2']), 'incorrect'

    assert prepare_matrix([['E', 'F'], ['2', 'D', 'E']],
                          0) == [['0', 'E', 'F'], ['2', 'D', 'E']], 'incorrect'
    assert prepare_matrix([['1', 'E', 'F'], ['1', 'E']],
                          0) == [['1', 'E', 'F'], ['0', '1', 'E']], 'incorrect'
    assert prepare_matrix([['1', 'E', 'F'], ['E']], 0) == [['1', 'E', 'F'],
                                                           ['0', '0',
                                                            'E']], 'incorrect'

    index_l2 = -1
    index_l1 = -1
    result.clear()
    res_line.clear()
    res = []
    assert mul_num_line2(['2', 'E', 'F', '4'],
                         2) == deque(['5', 'D', 'E', '8']), 'incorrect'

    index_l2 = -1
    index_l1 = -1
    result.clear()
    res_line.clear()
    res = []
    assert mul_num_line1(['4', '5', '2'], ['2', '1']) == [['4', '5', '2'],
                                                          ['8', 'A', '4',
                                                           '0']], 'incorrect'

    index_l2 = -1
    index_l1 = -1
    result.clear()
    res_line.clear()
    res = []
    assert sum_num(['2', '4'], ['E', 'F', '2']) == f'Сумма: F16', 'incorrect'

    index_l2 = -1
    index_l1 = -1
    result.clear()
    res_line.clear()
    res = []
    assert mul_num(['2', 'E', 'F', '4'],
                   ['2', 'D', 'E']) == f'Произведение: 869F98', 'incorrect'
    assert mul_num(['2', 'E', 'F', '4'],
                   ['2']) == f'Произведение: 5DE8', 'incorrect'
    print('Test: OK\n')


def sum_num(num_line1, num_line2):
    global k, hex, sum, j, res_matrix
    result.clear()
    res = [num_line1, num_line2]
    prepare_matrix(res, 0)
    res_matrix = np.array(res)
    col = len(res[-1]) - 1
    sum_matrix(res_matrix, col)
    return f"Сумма: {''.join(result)}"


def sum_matrix(res_matrix, col):
    global k
    if col >= 0:
        for index_l1 in res_matrix[:, col]:
            res_line.append(hex.index(index_l1))
        result.appendleft(hex[(sum(res_line) + k) % 16])
        k = (sum(res_line) + k) // 16 if (sum(res_line) + k) > 15 else 0
        col -= 1
        res_line.clear()
        sum_matrix(res_matrix, col)
    else:
        while k:
            result.appendleft(hex[k % 16])
            k = k // 16 if k > 15 else 0
            res_line.clear()
    return result


def prepare_matrix(res, i):
    max_len = len(max(res, key=len))
    if i != len(res):
        if i != max_len:
            res[i] = (['0'] * (max_len - len(res[i]))) + res[i]
            i += 1
        prepare_matrix(res, i)
    return res


def mul_num(num_line1, num_line2):
    global k, hex, index_l2, i, j, res_matrix, res
    res = []
    index_l2 = -1
    result.clear()
    mul_num_line1(num_line1, num_line2)
    prepare_matrix(res, 0)
    res_matrix = np.array(res)
    col = len(res[-1]) - 1
    sum_matrix(res_matrix, col)
    return f"Произведение: {''.join(result)}"


def mul_num_line1(num_line1, num_line2):
    global k, hex, res, res_line, index_l1, index_l2, num_i, num_j
    if index_l2 >= -len(num_line2):
        num_i = hex.index(num_line2[index_l2])
        index_l1 = -1
        a = mul_num_line2(num_line1, num_i)
        res.append(list(a))
        res_line.clear()
        index_l2 -= 1
        mul_num_line1(num_line1, num_line2)
    return res


def mul_num_line2(num_line1, num_i):
    global k, hex, res_line, index_l1, index_l2, num_j
    if index_l1 >= -len(num_line1):
        num_j = hex.index(num_line1[index_l1])
        if index_l1 == -1:
            res_line.extend(['0'] * (index_l2 * (-1) - 1))
        res_line.appendleft(hex[(num_i * num_j + k) % 16])
        k = (num_i * num_j + k) // 16 if (num_i * num_j + k) > 15 else 0
        index_l1 -= 1
        mul_num_line2(num_line1, num_i)
    else:
        while k:
            res_line.appendleft(hex[k % 16])
            k = k // 16 if k > 15 else 0
    return res_line


test()
n1, n2 = input('Введите 2 числа:').split(' ')
num_line1 = list(n1)
num_line2 = list(n2)

print(sum_num(num_line1, num_line2))
print(mul_num(num_line1, num_line2))

