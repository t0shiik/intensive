# Зотов Антон Иванович
# 1 вариант
# 13. Напишите функцию для нахождения НОД произвольного количества чисел

def search_NOD(*args):
    if len(args) == 0:
        return None
    result = args[0]
    for num in args:
        while num:
            result, num = num, result % num
    return result

# Пример использования
print(search_NOD(9, 33, 48))
print(search_NOD(10, 150, 255))

# Результат
# 3
# 5
