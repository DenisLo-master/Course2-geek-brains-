# 1. Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N, состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.

import hashlib

def test():
  assert count_substring('abc')==f'5 различных подстрок в строке abc', 'incorrect'
  print('Test: OK\n')



def count_substring(string):
  sum_substring = set()
  for i in range(len(string)):
      for j in range(i+1, len(string)+1):
          hash_str = hashlib.sha1(string[i:j].encode('ASCII')).hexdigest()
          sum_substring.add(hash_str)
  return (f'{len(sum_substring) -1} различных подстрок в строке {string}')

test()
print('Введите строку состоящую из маленьких латинских букв:')
s = input()
print(count_substring(s))