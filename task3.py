# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.

# Пример:

# - Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
#         Сумма 9.06


n = int(input())

dist_num = {}   # {} словарь

for i in range(1,n+1):

    dist_num[i] = round(((1+1/i)**i),2)

print(dist_num)

print(sum(dist_num.values()))