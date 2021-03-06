# Библиотека для случайных чисел
import random

name = input("Привет! Введи свое имя: ")
print('Здравствуйте, ' + name + '!')

# Обьявление первой комнаты
def roomone():
    way = input("Пойти налево: 1, пойти направо: 2. Ваш выбор: ")
	
	# Если игрок выбрал путь ...
    if way == '1':
        print("Вы пошли налево")
        print("Вы упали в обрыв :(")
        restart()
        
    if way == '2':
        print("Вы пошли направо")
        roomtwo()

# Обьявление второй комнаты
def roomtwo():
    print("Вы нашли сундук с золотом. Для открытия решите пример:")
	
	# Случайные числа для примера
    a = random.randint(1, 30)
    b = random.randint(1, 30)
	
	# Пример
    print(str(a) + ' + ' + str(b) + ' * 2')
    
    math = input('Ответ: ')
	
	# Формула примера
    answer = a+b*2
	
	# Проверка ответа
    if math == str(answer):
        print('Вы получили золото!')
        restart()
    else:
        print("Сундук не открытлся :(")
        roomtwo()

# Обьявление функции перезапуска игры
def restart():
    answer = input("Если вы хотите начать игру заново, введите ДА: ")
    if answer == 'ДА':
        roomone()
    else:
        print("Игра закончена. До свидания!")

# Вызов первой функции
roomone()
