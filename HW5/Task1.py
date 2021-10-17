#1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.
import collections
import pprint
from collections import namedtuple

companies = {}
Profit_company = collections.namedtuple(
    'Profit',
    ['quarter1', 'quarter2', 'quarter3', 'quarter4', 'temp_sum_year'])


# def test():
#     test_dict = {
#         'q':
#         Profit(quarter1=1, quarter2=2, quarter3=3, quarter4=4,
#                temp_sum_year=0),
#         'w':
#         Profit(quarter1=2, quarter2=3, quarter3=4, quarter4=5,
#                temp_sum_year=0),
#         'e':
#         Profit(quarter1=3, quarter2=4, quarter3=5, quarter4=6, temp_sum_year=0)
#     }
#     assert avrg_company(
#         test_dict
#     ) == f"\nСредняя прибыль в год: 6.0\n\nПрибыль ниже среднего:\n  'q: 4'\n\nПрибыль выше среднего:\n  'w: 8'", 'incorrect'
#     print('Test: OK\n')


def avrg_company(companies):
    sum_c = 0
    avrg_above = {}
    avrg_below = {}
    for n in companies:
        s = sum(companies[n])
        companies[n] = companies[n]._replace(temp_sum_year=s)
        sum_c += s
    avrg = sum_c / len(companies)
    for n in companies:
        s = companies[n].temp_sum_year
        if s < avrg:
            avrg_below[n] = s
        else:
            avrg_above[n] = s
        companies[n] = companies[n]._replace(temp_sum_year=0)
    avrg = f'\nСредняя прибыль в год: {avrg}'
    avrg_b = '\n  '.join('%s : %s' % (k, avrg_below[k])
                         for k in avrg_below.keys())
    avrg_a = '\n  '.join('%s : %s' % (k, avrg_above[k])
                         for k in avrg_above.keys())
    return f"\n{avrg}\n\nПрибыль ниже среднего:\n  {avrg_b}\n\nПрибыль выше среднего:\n  {avrg_a}"


def reg_company(count):
    while count:
        name = input('\n\nНазвание компании: ')
        count -= 1
        companies[name] = Profit_company(int(input('\nПрибыль\nкв1: ')),
                                         int(input('кв2: ')),
                                         int(input('кв3: ')),
                                         int(input('кв4: ')), 0)
    return companies


n = int(input('Количество компаний: '))
reg_company(n)
print(avrg_company(companies))
