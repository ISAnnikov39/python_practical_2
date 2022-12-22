# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
#Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

import random

n = int(input())
list_num = [random.randint(-n,n) for i in range(n)]
print(list_num)


file = open("File.txt","r")

result = 0

list_str = file.readline()

list_num = list(map(str.strip,list_str))

print(list_num)

list_num=list(map(int,list_num))

print(list_num)

for i in file:
    result *= list_num [int(i)]
print (result)