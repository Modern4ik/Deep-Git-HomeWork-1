# Поиск среднего арифметического из элементов списка.

from random import randint

print(my_list := [randint(1, 10) for _ in range(
    int(input("Введите кол-во элементов списка: ")))])

value_sum = 0

for i in my_list:
    value_sum += i

avg = round(value_sum / len(my_list),1)

print("{} - полученное значение среднего арифметического данного списка".format(avg))