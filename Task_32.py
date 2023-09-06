# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума). Список можно задавать рандомно

# На входе : [ 1, 5, 88, 100, 2, -4]
# 33
# 200
# Ответ: [2, 3]

from random import randint

def input_min_max():
    min = int(input("Введите минимум: "))
    max = int(input("Введите максимум: "))
    return min, max

def rnd_list(): return [randint(1,10) for i in range(1, 10)]
def find_min_to_max(list, min, max): return [x for x in list if min <= x <= max]

list_rnd = rnd_list()
min, max = input_min_max()
print(list_rnd)
print(min, max)
print(find_min_to_max(list_rnd, min, max))

