#Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.


def order_letter(l1, l2):
    o_l1 = ord(l1.lower()) - 96
    o_l2 = ord(l2.lower()) - 96
    count_l = abs(int(o_l1) - int(o_l2)) - 1
    return o_l1, o_l2, count_l


def test():
    assert order_letter('a', 'z') == (1, 26, 24), 'incorrect'
    assert order_letter('b', 'd') == (2, 4, 1), 'incorrect'
    assert order_letter('f', 'f') == (6, 6, -1), 'incorrect'
    print(f'Test: OK\n')


test()


try:
    l1, l2 = map(
        str,
        input('Введите 2 любые буквы английского алфавита: ').split(' '))
except ValueError:
    print('\nОШИБКА: Введите толькко 2 буквы, разделив их пробелом')
    exit()

o_l1, o_l2, count_l = order_letter(l1, l2)

if count_l == -1:
    print(f'Порядковый номер буквы в алфавите:\n{l1} = {o_l1}')
else:
  print(
    f'Порядковый номер буквы в алфавите:\n{l1} = {o_l1}\n{l2} = {o_l2}\nКоличество символов между буквами = {count_l}'
)
