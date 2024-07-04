import random

print('Добро пожаловать в числовую угадайку')


def welcome():
    global r_line
    r_line = input('Введите правую границу для случайного числа:')
    global num1
    num1 = random.randint(1, int(r_line))
    is_valid_n()


def is_valid(s):
    return s.isdigit() and 1 <= int(s) <= int(r_line)


def is_valid_n():
    while True:
        global n
        n = input('Введите число:')
        if is_valid(n):
            return
        else:
            print('А может быть все-таки введем целое число от 1 до 100?')


def game():
    welcome()
    count = 0
    while True:
        if int(n) < num1:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            count += 1
            is_valid_n()
        if int(n) > num1:
            print('Ваше число больше загаданного, попробуйте еще разок')
            count += 1
            is_valid_n()
        if int(n) == num1:
            count += 1
            print(f'Вы угадали, поздравляем! Количество попыток: {count}')
            restart = input('Хотите сыграть еще раз? Да или нет?')
            if restart.lower() in 'да':
                game()
            else:
                return


game()
