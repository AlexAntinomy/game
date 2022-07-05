
from random import randint
print("Угадай где привидение")
feeling_brave = True
score = 0
while feeling_brave:
    ghost_door = randint(1, 3)
    print("Перед тобой три двери...")
    print("За одной из них привидение")
    print("Какую выберешь ты?")
    door = input('1, 2, или 3?')
    door_num = int(door)
    if door_num == ghost_door:
         print("Вот же оно!")
         feeling_brave = False
    else:
        print("Здесь ничего нет!")
        print("Посмотри в другой комнате...")
        score = score + 1
print("Беги!")
print("Игра окончена! Ты набрал", score, "очков")