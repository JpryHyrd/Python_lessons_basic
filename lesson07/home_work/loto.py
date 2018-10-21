#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""
# ==Loto==
import random
#Создаю генератор рандомных чисел для карточек
def cards():
#Рандомные числа буду помещать в списки
	a = []
	b = []
	c = []
#С помощью цикла для добавляю рандомные числа в списки
	for i in range(5):
		a.append(random.randint(1, 91))
		b.append(random.randint(1, 91))
		c.append(random.randint(1, 91))
#Сортирую добавленные числа по возрастанию
		a.sort()
		b.sort()
		c.sort()
#Добавляю эти списки в кортэдж
	l = (a, b, c)
	return l
#Создаю карточки для игрока и бота
player_card = cards()
computer_card = cards()
#В этой функции я создаю внешний вид карточек, которые будет видеть пользователь на экране
def print_(a, b, c):
#Ограничитель 
	print("- " * 7)
#Первая строка
	if len(a) == 5:
		print(str(a[0]) + " " + str(a[1]) + " " + str(a[2]) + " " + str(a[3]) + " " + str(a[4]))
	elif len(a) == 4:
		print(" " + str(a[0]) + " " + str(a[1]) + " " + str(a[2]) + " " + str(a[3]) + " ")
	elif len(a) == 3:
		print(" " + str(a[0]) + "  " + str(a[1]) + "  " + str(a[2]) + " ")
	elif len(a) == 2:
		print("  " + str(a[0]) + "  " + str(a[1]) + "   ")
	elif len(a) == 1:
		print("    " + str(a[0]) + "    ")
	elif len(a) == 0:
		print(" ")
#Вторая строка
	if len(b) == 5:
		print(str(b[0]) + " " + str(b[1]) + " " + str(b[2]) + " " + str(b[3]) + " " + str(b[4]))
	elif len(b) == 4:
		print(" " + str(b[0]) + " " + str(b[1]) + " " + str(b[2]) + " " + str(b[3]) + " ")
	elif len(b) == 3:
		print(" " + str(b[0]) + "  " + str(b[1]) + "  " + str(b[2]) + " ")
	elif len(b) == 2:
		print("  " + str(b[0]) + "  " + str(b[1]) + "   ")
	elif len(b) == 1:
		print("    " + str(b[0]) + "    ")
	elif len(b) == 0:
		print(" ")
#Третья строка 
	if len(c) == 5:
		print(str(c[0]) + " " + str(c[1]) + " " + str(c[2]) + " " + str(c[3]) + " " + str(c[4]))
	elif len(c) == 4:
		print(" " + str(c[0]) + " " + str(c[1]) + " " + str(c[2]) + " " + str(c[3]) + " ")
	elif len(c) == 3:
		print(" " + str(c[0]) + "  " + str(c[1]) + "  " + str(c[2]) + " ")
	elif len(c) == 2:
		print("  " + str(c[0]) + "  " + str(c[1]) + "   ")
	elif len(c) == 1:
		print("    " + str(c[0]) + "    ")
	elif len(c) == 0:
		print(" ")
	print("- " * 7)
#Создаю пустой список, чтобы помещать туда уже использованные числа
list_b = []
#Переменная а будет использовться в цикле вкачестве переменной, принимающей ответ пользователя
a = None
while True:
#Проверка состояния игры на данный момент:
#Ничья
	if len(computer_card[0]) == 0 and len(computer_card[1]) == 0 and len(computer_card[2]) == 0\
	and len(player_card[0]) == 0 and len(player_card[1]) == 0 and len(player_card[2]) == 0:
		print("\n\t\t===Draw===")
		print("\nPlayer card")
		print_(player_card[0], player_card[1], player_card[2])
		print("\nComputer card")
		print_(computer_card[0], computer_card[1], computer_card[2])
		break
#Победа бота
	elif len(computer_card[0]) == 0 and len(computer_card[1]) == 0 and len(computer_card[2]) == 0:
		print("\n\t\t===Computer won===")
		print("\nComputer card")
		print_(computer_card[0], computer_card[1], computer_card[2])
		break
#Победа игрока
	elif len(player_card[0]) == 0 and len(player_card[1]) == 0 and len(player_card[2]) == 0:
		print("\n\t\t===You won===")
		print("\nPlayer card")
		print_(player_card[0], player_card[1], player_card[2])
		break
#Создаю рандомное число(бочонок с номером)
	num = random.randint(1, 90)
#Проверяю, было ли число использовано ранее
	if num in list_b:
#Если число было использовано, возвращаюсь в начало цикла 
		continue
#Если число не использовалось ранее, то добавляю его в список,
#чтобы оно не было использовано в дальнейшем
	list_b.append(num)
#Вывожу это число(номер бочонка) на экран
	print("\nNumber - " + str(num))
#Вывожу карточку игрока
	print("\nPlayer card")
#Сдесь использую написанную ранее функцию вывода карточки
	print_(player_card[0], player_card[1], player_card[2])
#Карточка бота
	print("\nComputer card")
#Та же функция, что и для игрока(Вывод карточки)
	print_(computer_card[0], computer_card[1], computer_card[2])
#Спрашиваю пользователя о его далянейшем действии и передаю ответ в переменную а:
#1 - Зачеркнуть
#Enter - продолжить
#3 - выйти из игры
	a = input("1 - Cross out; Enter - Continue; 3 - Exit:  ")
#Если он хочет выйти, то прощаюсь с ним и завершаю цикл
	if a == "3":
		print("Good by!")
		break
#Чит код, присваивающий победу игроку
	elif a == "qwerty":
		print("\n\t\t\a$$===YOU WIN===$$")
		break
#Если он хочет зачеркнуть чило(Номер бочонка), то выполняю следующие действия:
	elif a == "1":	
#Проверяю, есть ли это число в его карточке
		if num in player_card[0] or num in player_card[1] or num in player_card[2]:
#Если оно есть то пытаюсь его удалить:
#Я не знаю, в какой именно строке это число и сколько этих чисел,
#создавать несколько условий, чтобы узнать где именно оно находится
#и сколько этих чисел, очень долго. Поэтому я добавляю действия в 
#конструкцию try, и прописываю команду удаления 5 раз для каждой строки
#(вдруг в одной строке будет 5 одинаковых чисел)
			try:
				player_card[0].remove(num)
				player_card[0].remove(num)
				player_card[0].remove(num)
				player_card[0].remove(num)
				player_card[0].remove(num)
			except Exception:
				pass
			try:
				player_card[1].remove(num)
				player_card[1].remove(num)
				player_card[1].remove(num)
				player_card[1].remove(num)
				player_card[1].remove(num)
			except Exception:
				pass
			try:
				player_card[2].remove(num)
				player_card[2].remove(num)
				player_card[2].remove(num)
				player_card[2].remove(num)
				player_card[2].remove(num)
			except Exception:
				pass
#Если в карточке игрока этого числа нет, то осведомляю игрока о поражении
# и завершаю цикл
		else:
			print("You've lost!")
			break
#Ели игрок нажал Enter(при нажатии этой клавиши передается пустая строка),
#то произвожу проверки:

#Проверяю, есть ли это число в его карточке, если есть, то сообщаю ему о поражении
	elif a == "":
		if num in player_card[0] or num in player_card[1] or num in player_card[2]:
			print("You've lost!")
			break
#Еслт этого числа нет, то ничего не делаю
		else:
			pass
#Если пользователь нажал не на ту клавишу, то сообщая ему об ошибке и завершаю игру
	else:
		print("\aA data-entry error!")
		break
#Если это число есть в карточку бота, то, аналогично с карточкой игрока, удаляю его
	if num in computer_card[0] or num in computer_card[1] or num in computer_card[2]:
		try:
			computer_card[0].remove(num)
			computer_card[0].remove(num)
			computer_card[0].remove(num)
			computer_card[0].remove(num)
			computer_card[0].remove(num)
		except Exception:
			pass
		try:
			computer_card[1].remove(num)
			computer_card[1].remove(num)
			computer_card[1].remove(num)
			computer_card[1].remove(num)
			computer_card[1].remove(num)
		except Exception:
			pass
		try:
			computer_card[2].remove(num)
			computer_card[2].remove(num)
			computer_card[2].remove(num)
			computer_card[2].remove(num)
			computer_card[2].remove(num)
		except Exception:
			pass
#THE END!!!!
