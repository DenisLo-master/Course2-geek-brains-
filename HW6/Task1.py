# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.

# Блок-схема- алгоритм (открывать в google chrome)
# https://www.figma.com/file/O2kjffn4ZUP4fR3Qcs2UmO/HW3-Task6?node-id=0%3A1
import sys


def sum_between1(list1):
    try:
        list1 = list(map(int, list1))
        _list = list1.copy()
        _list.sort()
        min_n = list1.index(_list[0])
        max_n = list1.index(_list[-1])
        res = 0
        for _num in range(len(_list)):
            if _list[_num] == list1[min_n] or _list[_num] == list1[max_n]:
                _list[_num] = 0
            else:
                res += _list[_num]
        print('--- res - ', sys.getsizeof(res),
              sys.getrefcount(res))  # 28 байт, 7 ссылок
        print('--- _list - ', sys.getsizeof(_list),
              sys.getrefcount(_list))  ##152 байта = 56+12*8, 2 ссылки
        print('--- max_n - ', sys.getsizeof(max_n),
      sys.getrefcount(max_n))  # 28 байт, 38 ссылок
        print('\n\n--- list1 - ', sys.getsizeof(list1),
      sys.getrefcount(list1))  #152 байта = 56+12*8, 4 ссылки
        return f'\n\nСписок: {list1}\nСумма между min({list1[min_n]}) и max({list1[max_n]}): {res}'
    except ValueError or TypeError:
        return f'\nОШИБКА: необходимо передать только массив чисел'


######


def sum_between2(list1):
    try:
        list1 = list(map(int, list1))
        print(list1)
        list1.sort()
        min_n = list1[0]
        max_n = list1[-1]
        while min_n in list1:
            list1.remove(min_n)
        while max_n in list1:
            list1.remove(max_n)

        print('--- res - не используется') 
        print('--- _list - не используется')
        print('--- max_n - ', sys.getsizeof(max_n),
      sys.getrefcount(max_n))  # 28 байт, 38 ссылок
        print('\n\n--- list1 - ', sys.getsizeof(list1),
      sys.getrefcount(list1))  #152 байта = 56+12*8, 4 ссылки
        return f'\nСумма между min({min_n}) и max({max_n}): {sum(list1)}'
    except ValueError or TypeError:
        return f'\nОШИБКА: необходимо передать только массив чисел'


list1 = [7, 3, 3, 6, 6, 4, 10, 15, 77, 3, 8, 9]
print('\nВариант1 ', sum_between1(list1))



print('\n', '-' * 20, '\n')

print('\nВариант2 ', sum_between2(list1))

print('\n Версия- Python 3.8.12\n OS- BigSur\nПервая задача: представлено 2 варианта приводящиее к одному и тому же результату, но использующие различное количество переменных и соответственно памяти',
'\nВыделено памяти: \n  Вариант 1 = 388 байт\n  Вариант 2 = 208 байт\n')

print('\n', '/' * 60, '\n')

#1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

# Блок-схема- алгоритм (открывать в google chrome)
# https://www.figma.com/file/OHXDhFDLAeqTMVML2Qb5gP/HW3-Task1?node-id=0%3A1


def multiple_digit1(value1, value2):
    try:
        value = range(value1, value2)
        print('--- value - ', sys.getsizeof(value),
              sys.getrefcount(value))  #48 байт, 2 ссылки
        if value1 == value2:
            raise TypeError
        res = []
        for _i in range(2, 10):
            count_n = []
            for _num in value:
                if _num % _i == 0:
                    count_n.append(_num)
            res.append(f'Кол. чисел кратно {_i}: {len(count_n)}')
        print('--- count_n - ', sys.getsizeof(count_n),
              sys.getrefcount(count_n))  #184 байта = 56+16*8, 2 ссылки
        print('--- res - ', sys.getsizeof(res),
              sys.getrefcount(res))  # 120 байт = 56+8*8, 2 ссылки
        print('--- value1 - ', sys.getsizeof(value1),
              sys.getrefcount(value1))  # 28 байт, 135 ссылок
        print('--- _num - ', sys.getsizeof(_num),
              sys.getrefcount(_num))  # 28 байт, 5 ссылок
        print('--- _i - ', sys.getsizeof(_i),
              sys.getrefcount(_i))  # 28 байт, 18 ссылок
        return f'\nДиапазон {value1}:{value2-1}\n\n' + '\n'.join(res)
    except TypeError:
        return f'\nОШИБКА: необходимо передать только диапазон чисел'


######


def multiple_digit2(value1, value2):
    try:
        value = range(value1, value2)
        print('--- value - ', sys.getsizeof(value),
              sys.getrefcount(value))  #48 байт-диапазон не зависимо от границ, 2 ссылки
        if value1 == value2:
            raise TypeError
        res = []
        for _i in range(2, 10):
            count_n = 0
            for _num in value:
                if _num % _i == 0:
                    count_n += 1
            res.append(f'Кол. чисел кратно {_i}: {count_n}')
        print('--- count_n - ', sys.getsizeof(count_n),
              sys.getrefcount(count_n))  #28 байта, 15 ссылки
        print('--- res - ', sys.getsizeof(res),
              sys.getrefcount(res))  # 120 байт = 56+8*8, 2 ссылки
        print('--- value1 - ', sys.getsizeof(value1),
              sys.getrefcount(value1))  # 28 байт, 135 ссылок
        print('--- _num - ', sys.getsizeof(_num),
              sys.getrefcount(_num))  # 28 байт, 5 ссылок
        print('--- _i - ', sys.getsizeof(_i),
              sys.getrefcount(_i))  # 28 байт, 18 ссылок
        return f'\nДиапазон {value1}:{value2-1}\n\n' + '\n'.join(res)
    except TypeError:
        return f'\nОШИБКА: необходимо передать только диапазон чисел'


value1 = 2
value2 = 100

print('\nВариат1', multiple_digit1(value1, value2))
print('\n', '-' * 20, '\n')
print('\nВариат2', multiple_digit2(value1, value2))

print('\nВторая задача: представлено 2 варианта приводящиее к одному и тому же результату, но занимающие различное количество памяти для некоторых переменных из за использования разных типов переменных',
'\nВыделено памяти: \n  Вариант 1 = 464 байт\n  Вариант 2 = 308 байт\n')

