# Задача XO необязательная.
# Сделайте игру крестики - нолики, человек должен играть с ботом, поле 3*3.
# Конечно, бот не должен ходить на занятые поля
# Если есть желание, то можете наделить бота псевдоинтеллектом,чтоб он ходил как можно ближе к своим занятым клеткам
# После каждого хода на экран должна выводиться текущая обстановка на поле.
from random import randint

def print_new_ground(ground):
    for row in ground :
        for el in row:
            print(el, end=' ')
        print()

def gamers_move():
    row = int(input("Введите номер стоки: "))-1
    colon = int(input("Введите номер столбца: "))-1
    while ground[row][colon] != '_':
        print('Поле уже занято')
        row = int(input("Введите номер стоки: "))-1
        colon = int(input("Введите номер столбца: "))-1
    return row, colon

def bot_move(ground):
    row = randint(0,2)
    colon = randint(0,2)
    while ground[row][colon] != '_':
        row = randint(0,2)
        colon = randint(0,2)
    return row, colon

def write_on_ground(ground ,row, colon, X_or_O):
    ground[row][colon] = X_or_O
    return ground

def win_check(ground):
    if ground[0][0] == ground[0][1] == ground[0][2] == 'X' or ground[1][0] == ground[1][1] == ground[1][2]== 'X' or ground[2][0] == ground[2][1] == ground[2][2]== 'X' or ground[0][0] == ground[1][0] == ground[2][0]== 'X' or ground[0][1] == ground[1][1] == ground[2][1]== 'X' or ground[0][2] == ground[1][2] == ground[2][2]== 'X' or ground[0][0] == ground[1][1] == ground[2][2]== 'X' or ground[0][2] == ground[1][1] == ground[2][0]== 'X': 
        print("Мешок с костями победил")
    elif ground[0][0] == ground[0][1] == ground[0][2] == 'O' or ground[1][0] == ground[1][1] == ground[1][2]== 'O' or ground[2][0] == ground[2][1] == ground[2][2]== 'O' or ground[0][0] == ground[1][0] == ground[2][0]== 'O' or ground[0][1] == ground[1][1] == ground[2][1]== 'O' or ground[0][2] == ground[1][2] == ground[2][2]== 'O' or ground[0][0] == ground[1][1] == ground[2][2]== 'O' or ground[0][2] == ground[1][1] == ground[2][0]== 'O': 
        print("Победа Бота!!!")

def conditions_of_win(ground):
    if ground[0][0] == ground[0][1] == ground[0][2] != '_' or ground[1][0] == ground[1][1] == ground[1][2]!= '_' or ground[2][0] == ground[2][1] == ground[2][2]!= '_' or ground[0][0] == ground[1][0] == ground[2][0]!= '_' or ground[0][1] == ground[1][1] == ground[2][1]!= '_' or ground[0][2] == ground[1][2] == ground[2][2]!= '_' or ground[0][0] == ground[1][1] == ground[2][2]!= '_' or ground[0][2] == ground[1][1] == ground[2][0]!= '_' : 
        return False
    else: 
        return True

ground = [['_','_','_'],['_','_','_'],['_','_','_']]
print_new_ground(ground)
while conditions_of_win(ground) != False:
    row, colon = gamers_move()
    write_on_ground(ground ,row, colon, 'X')
    print('Поле после хода игрока')
    print_new_ground(ground)
    win_check(ground)
    row, colon = bot_move(ground)
    write_on_ground(ground ,row, colon, 'O')
    print('Поле после хода бота')
    print_new_ground(ground)
    win_check(ground)

    