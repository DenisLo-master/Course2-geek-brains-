# 7. По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника, составленного из этих отрезков. Если такой треугольник существует, то определить, является ли он разносторонним, равнобедренным или равносторонним.

def triangle_type(a, b, c):
  try:
      if a + b < c or a + c < b or b + c < a:
        raise AttributeError
      elif a == b or b == c or a == c:
          if a == b == c:
              return '\nТреугольник - раВносторонний'
          return '\nТреугольник - равнобедренный'
      else:
          return '\nТреугольник - раЗносторонний'
  except AttributeError:
      print(
          '\nОШИБКА: Сумма любых двух отрезков должна быть больше длины 3-го отрезка'
      )
      exit()
  

def test():
    assert triangle_type(3,4,5)=='\nТреугольник - раЗносторонний', 'incorrect'
    assert triangle_type(3,3,5)=='\nТреугольник - равнобедренный', 'incorrect'
    assert triangle_type(5,5,5)=='\nТреугольник - раВносторонний', 'incorrect'
    #assert triangle_type(1,1,5)==False, 'icorrect'
    print(f'Test: OK\n')


test()
try:
    a, b, c = map(
        float,
        input('Введите длины 3-х отрезков для проверки треугольника: ').split(
            ' '))
except ValueError:
    print(
        '\nОШИБКА: Введите цифровые значение длин для каждой стороны треугольника, разделив их пробелом'
    )
    exit()

tr_type = triangle_type(a, b, c)
print(tr_type)
