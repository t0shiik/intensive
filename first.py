# Зотов Антон Иванович
# 1 вариант
#1. Декоратор считающий количество вызовов функции

def count_calls(func):
    count = 0
    def check(*args):
        nonlocal count
        count += 1
        print(f'Функция {func.__name__} была вызвана {count} раз')
        return func(*args)

    return check

# Пример использования
@count_calls
def Hello(name):
    print(f'Hello, {name}')

Hello('Anton')
Hello('Hasbik')
Hello('Danilka')

# Результат
# Функция Hello была вызвана 1 раз
# Hello, Anton
# Функция Hello была вызвана 2 раз
# Hello, Hasbik