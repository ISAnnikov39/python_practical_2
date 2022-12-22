# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

number = float(input("введите число "))

length_number = len(str(number))

result = 0

while number != int(number):

    number= round(number*10,length_number-1)


while number >0:

    result += number%10

    number = number //10

print (result)

