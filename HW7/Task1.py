#1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).

from random import randint
import time

res = 0


def test():
    assert sort_bubble1([10, 20, 30, 40, 50, 60, 70,
                         80]) == ([80, 70, 60, 50, 40, 30, 20,
                                   10], 21), 'incorrect'
    assert sort_bubble2([10, 20, 30, 40, 50, 60, 70,
                         80]) == ([80, 70, 60, 50, 40, 30, 20,
                                   10], 21), 'incorrect'
    assert sort_bubble1([70, 80, 60, 50, 40, 30, 20,
                         10]) == ([80, 70, 60, 50, 40, 30, 20,
                                   10], 21), 'incorrect'
    assert sort_bubble2([70, 80, 60, 50, 40, 30, 20,
                         10]) == ([80, 70, 60, 50, 40, 30, 20,
                                   10], 6), 'incorrect'
    print('Test: OK\n')


def sort_bubble1(list_1):
    global res
    i = 1
    max_l = len(list_1)
    step = []
    res = 0
    while i < max_l:
        for j in range(max_l - i):
            if list_1[j] < list_1[j + 1]:
                list_1[j], list_1[j + 1] = list_1[j + 1], list_1[j]
        step.append(j)
        i += 1
        res = sum(step)
    return list_1, res


def sort_bubble2(list_2):
    global res
    i = 1
    n = 0
    l = max_l = len(list_2)
    step = []
    res = 0
    while i < max_l:
        l = l - n - 1
        n = 0
        if l > 0:
            for j in range(l):
                if list_2[j] < list_2[j + 1]:
                    list_2[j], list_2[j + 1] = list_2[j + 1], list_2[j]
                    n = 0
                else:
                    n += 1
            step.append(j)
            i += 1
        else:
            break
        res = sum(step)
    return list_2, res


#lst = [10, 20, 30, 40, 50, 60, 70, 80]
#lst = [70, 80, 60, 50, 40, 30, 20, 10]

test()
lst = [randint(-100, 100) for i in range(0, 50)]

print(lst)

print('\n', '/' * 40, '\n')

list_1 = lst.copy()
list_2 = lst.copy()

a = time.time()
sort_bubble1(list_1)
print('time', time.time() - a)
print(f'Steps: {res}')
print(list_1)

print('-' * 20)

a = time.time()
sort_bubble2(list_2)
print('time', time.time() - a)
print(f'Steps: {res}')
print(list_2)

print('-' * 20)

print(list_1 == list_2)
