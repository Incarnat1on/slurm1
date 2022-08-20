import random

gueses_try = 0

name = input ('Приветствую путник! Назови свое имя \n')
number = random.randint(1, 100)
while gueses_try < 8:
    guess = int (input ('Введите Ваше число\n'))
    gueses_try+=1
    print (f'Попытка №{gueses_try}')
    if guess<number:
        print ("Не правильно! Загаданное число больше!")
    elif guess>number:
        print ('Не правильно! Загаданное число меньше!')
    elif guess==number:
        print ('Вы победили!')
        break
    else:
        print (f'А вот и не угадал! Я загадал число {number}')
