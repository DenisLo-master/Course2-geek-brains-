#2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
from random import randint

def test():
      assert merge_sort([5, 8, 1, 3, 4, 7, 6])==[1, 3, 4, 5, 6, 7, 8], 'incorrect'
      assert merge_sort([8, 7, 6, 5, 4, 3, 1])==[1, 3, 4, 5, 6, 7, 8], 'incorrect'  
      print('Test: OK\n')

def merge_sort(A):
    if len(A) <= 1:
        return A
    L, R = A[:len(A) // 2], A[len(A) // 2:]
    merge_sort(L)
    merge_sort(R)
    n = m = k = 0
    C = [0] * (len(L) + len(R))
    while n < len(L) and m < len(R):
        if L[n] <= R[m]:
            C[k] = L[n]
            n += 1
        else:
            C[k] = R[m]
            m += 1
        k += 1
    while n < len(L):
        C[k] = L[n]
        n += 1
        k += 1
    while m < len(R):
        C[k] = R[m]
        m += 1
        k += 1
    for i in range(len(A)):
        A[i] = C[i]
    return A


test()
lst = [randint(0, 50) for i in range(0, 50)]
print(lst)
print()
print(merge_sort(lst))
