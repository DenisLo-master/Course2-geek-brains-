# 2. Написать два алгоритма нахождения i-го по счёту простого числа.

# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»
# Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов. Результаты анализа сохранить в виде комментариев в файле с кодом.

import time


def time_func(func):
    def wrapper():
        start_time = time.time()
        res = func()
        end_time = time.time()
        print('\nВремя исполнения', end_time - start_time)
        return res

    return wrapper


@time_func
def prime_lenear():
    global i
    j = 1
    numbers = [2]
    prime = [2]
    while len(prime) < i:
        value_prime = False
        j += 1
        numbers.append(j)
        for k in range(2, len(numbers), 1):
            if j % k == 0 and j / k != 1:
                value_prime = False
                break
            value_prime = True
        if value_prime:
            prime.append(j)
    return f'prime_lenear(): i = {prime[i - 1]}'


@time_func
def eratosthenes():  # n - число, до которого хотим найти простые числа
    global i
    sieve = list(range(30))
    sieve[1] = 0  # без этой строки итоговый список будет содержать единицу
    for m in sieve:
        if m > 1:
            for j in range(m + m, len(sieve), m):
                sieve[j] = 0
    sieve1 = [x for x in sieve if x != 0]
    return f'eratosthenes(): i = {sieve1[i - 1] if len(sieve1) >= i - 1 else None}'


i = 10
print(prime_lenear())
print(eratosthenes())


#Вывод
#сложность:
#  O(n2) для функции prime_lenear(), 
#  O(n*m) для функции eratosthenes(), 

# порядок роста:
#  O(1) для функции sum_between_all(), 
#  O(1) для функции sum_between_(), 