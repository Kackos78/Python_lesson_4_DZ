# Задача НЕГАФИБОНАЧЧИ по желанию
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

n = 15

def make_doble_fibonachi(n):
    list_1 = [-1,1,0,1,1]
    for i in range(3,n): list_1.append(list_1[-1] + list_1[-2])
    for i in range(-n, -3): list_1.insert(0, list_1[1] - list_1[0])
    return list_1

print(make_doble_fibonachi(n))