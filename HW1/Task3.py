#3. По введенным пользователем координатам двух точек вывести уравнение прямой вида y=kx+b, проходящей через эти точки.

def equation(x1, y1, x2, y2):
    k = (y1 - y2) / (x1 - x2)
    b = y2 - k * x2
    return k, b

while True:
  try:
      x1,y1=input('Введите координаты ПЕРВОЙ точки (x;y): ').split(';')
      x1,y1=map(int,[x1,y1])
  except ValueError:
      print('Введите х и y координаты, в формате ’x;y’')
  else:
    break

    
while True:
  try:
      x2,y2=input('Введите координаты ВТОРОЙ точки (x;y): ').split(';')
      x2,y2=map(int,[x2,y2])
      if x1-x2==0:
          raise ZeroDivisionError
  except ValueError:
      print('ОШИБКА: Введите х и y координаты, в формате ’x;y’')
  except ZeroDivisionError:
      print('ОШИБКА деелеения на 0: значения x1 и x2 совпадают')
  else:
    break


k,b=equation(x1,y1,x2,y2)
if b>0:
    print(f'Уравнение: y = {k} * x +{b}')
else:
    print(f'Уравнение: y = {k} * x {b}')



