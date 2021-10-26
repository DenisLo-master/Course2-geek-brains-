#3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы. Задачу можно решить без сортировки исходного массива. Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках

from random import randint

def test():
    assert median([0, 100, 5, 9, 8, 6, 2])==6,'incorrect'
    assert median([0, 1, 1, 1, 3, 4, 5])==1,'incorrect'
    assert median([0, 0, 0, 0, 49, 50, 100])==0,'incorrect'
    print('Test: OK\n')
    

def median(lst):
    m=0
    while m < len(lst):
        i=0
        l = r = 0
        while i < len(lst):
            if lst[m] >= lst[i] and m!=i:
                l+= 1
            if lst[m] <= lst[i] and m!=i:
                r += 1
            if l >= (len(lst) // 2) and r >= (len(lst) // 2):
                return lst[m]
            i+=1
        m+=1
    return


test()

m = randint(1, 5)
lst = [randint(0, 50) for i in range(0, (2 * m + 1))]

print(lst)
print(f'Медиана: {median(lst)}')
