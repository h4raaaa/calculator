def calculator():
    print('Простой калькулятор')
    a = float(input('Введите первое число: '))
    b = float(input('Введите второе число: '))

    print('Выберите операцию:')
    print('+  Сложение')
    print('-  Вычитание')
    print('*  Умножение')
    print('/  Деление')

    op = input('Операция: ')

    if op == '+':
        print('Результат:', a + b)
    elif op == '-':
        print('Результат:', a - b)
    elif op == '*':
        print('Результат:', a * b)
    elif op == '/':
        if b != 0:
            print('Результат:', a / b)
        else:
            print('Ошибка: деление на ноль')
    else:
        print('Неизвестная операция')

calculator()