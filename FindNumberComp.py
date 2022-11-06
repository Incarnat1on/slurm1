import random

gueses_try = 0

name = input ('Приветствую путник! Назови свое имя \n')
number = input (f'{name} Загадай число компьютеру от 0 до 100\n')
while gueses_try < 8:
    guess = random.randint(1, 100)
    gueses_try+=1
    print (f'Попытка №{gueses_try}')
    print (f'Это число {guess} ?')
    answer = input ()
    if answer == '=':
        print ('Ура я победил!')
        break
    elif answer == '-':
        print ('Попробуй еще разок Искуственный интелект :)')
    if gueses_try == 8:
        print (f'Высший разум победил! Я загадал число {number}')