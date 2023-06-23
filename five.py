# Зотов Антон Иванович
# 1 вариант
# 5. Найдите три ключа с самыми высокими значениями в словаре my_dict

def top_3_keys(my_dict):
    rev = sorted(my_dict, reverse=True)
    a, b, c, = rev[0], rev[1], rev[2]
    return a, b, c

# Пример функционирования
d1 = {1: 2, 2: 4, 3: 9, 4: 16, 5: 25}
d2 = {8: 'vosem', 3: 'tri', 7: 'sem', 2: 'dva', 5: 'pyat'}
print(top_3_keys(d1))
print(top_3_keys(d2))

# Результат
# (5, 4, 3)
# (8, 7, 5)