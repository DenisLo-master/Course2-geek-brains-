#Определить, является ли год, который ввел пользователем, високосным или не високосным.


def year_type(y):
    if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
        return True
    else:
        return False


def test():
    assert year_type(1985) == False, 'incorrect'
    assert year_type(2000) == True, 'incorrect'
    assert year_type(1700) == False, 'incorrect'
    assert year_type(1900) == False, 'incorrect'
    assert year_type(2020) == True, 'incorrect'
    print(f'Test: OK\n')


test()
try:
    y = int(input('Введите год: '))
except ValueError:
    print('\nОШИБКА: Вводите год в формате "ГГГГ"')
    exit()

if year_type(y) == True:
    print(f'\n{y}год - високосный')
else:
    print(f'\n{y}год - невисокосный')
