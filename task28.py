# Задача 28: Напишите рекурсивную функцию sum(a, b), 
# возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4

def sum(first, second):
    if first:
        return 1 + sum(first-1, second)
    elif second:
        return 1 + sum(first, second-1)
    else:
        return 0



print('Введите первое число: ')
a = input()
a = int(a)

print('Введите второе число: ')
b = input()
b = int(b)

c = sum(a, b)
print(c)