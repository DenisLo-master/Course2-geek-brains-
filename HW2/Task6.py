#6. В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10 попыток. После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число, чем то, что загадано. Если за 10 попыток число не отгадано, то вывести загаданное число.

from random import randint


def test():
    assert guess(
        90, 9,
        '90') == f'\nПоздравляю, ты угадал число, c 2-й попытки', 'incorrect'
    assert guess(
        33, 5,
        '33') == '\nПоздравляю, ты угадал число, c 6-й попытки', 'incorrect'

    # assert guess(
    #     15, 8, '30') == f'\nВаше число больше. Осталось попыток: 7', 'incorrect'
    # assert guess(
    #     40, 10, '22') == f'\nВаше число меньше. Осталось попыток: 3', 'incorrect'
    assert guess(
        40, 1, '10'
    ) == f'\nК сожалению, ты не угадал число, попытки закончились', 'incorrect'
    # assert guess(
    #     55, 6, '-32'
    # ) == f'\nОсталось попыток: 5\nОШИБКА: введите число в текущеем диапазоне 0 - 100\n', 'incorrect'
    # assert guess(
    #     60, 4, 'f'
    # ) == f'\nОсталось попыток: 3\nОШИБКА: введите число в текущеем диапазоне 0 - 100\n', 'incorrect'
    print('Test: OK')


def rand_value(start, stop):
    global f_value
    f_value = randint(left_b, right_b)
    return f_value


def guess(f_value, attempts, value):
    global left_b, right_b, result
    try:
        value = int(value)
        if left_b <= value <= right_b:
            if value == f_value:
                result=f'\nПоздравляю, ты угадал число, c {11-attempts}-й попытки'
            elif value < f_value and attempts > 1:
                left_b = value
                attempts -= 1
                print(f'\nВаше число меньше. Осталось попыток: {attempts}')
                guess(
                    f_value, attempts,
                    input(
                        f'\nТекущий Диапазон: {left_b} - {right_b}\nУгадайтее число: \n'
                    ))
            elif value > f_value and attempts > 1:
                right_b = value
                attempts -= 1
                print(f'\nВаше число больше. Осталось попыток: {attempts}')
                guess(
                    f_value, attempts,
                    input(
                        f'\nТекущий Диапазон: {left_b} - {right_b}\nУгадайтее число: \n'
                    ))
            else:
                result=f'\nК сожалению, ты не угадал число, попытки закончились'
        elif result != '':
            print(result)
            exit()
        else:
            raise ValueError
    except ValueError:
        attempts -= 1
        guess(
            f_value, attempts,
            input(
                f'\nОсталось попыток: {attempts}\nОШИБКА: введите число в текущеем диапазоне {left_b} - {right_b}\n'
            ))


left_b = 0
right_b = 100
attempts = 2
f_value = int
result=''
rand_value(left_b, right_b)

#test()
print(guess(f_value, attempts,
      input(f'\nТекущий Диапазон: {left_b} - {right_b}\nУгадайтее число: \n')))
