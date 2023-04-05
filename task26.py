# Задача 26:  Напишите программу, 
# которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

def exponention(osnovanie, pokazatel):
    if pokazatel == 0:
        return 1
    else:
        osnovanie = osnovanie*exponention(osnovanie, pokazatel-1)
    return osnovanie



print('Введите основание степени')
a = input()
a = int(a)

print('Введите показатель степени')
n = input()
n = int(n)

k = exponention(a, n)
print(k)
