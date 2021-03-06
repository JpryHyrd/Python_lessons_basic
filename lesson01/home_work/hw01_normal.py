
__author__ = 'Казаков Артур Владимирович'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.

i = 0
b = 0
while True:
	nom = input("Введите произвольное целое число:")
	if nom.isdigit():
		for i in range(len(nom) - 1):
			c = nom[i]
			c = int(c)
			if c > b:
				b = c
			else:
				pass
		b = str(b)
		print("\n\tНаибольшая цифра числа", nom, "-", b)
		break
	else:
		print("\aВы ввели не число. Повторите попытку снова!")
input()

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.

a = input("Введите значение первой переменной: ")
b = input("Введите значение второй переменной: ")
list = []
list.append(a)
list.append(b)
a = list[1]
b = list[0]
print("\nЯ поменял значения переменных местами, вот итог:")
print("\t\tЗначение 1 -", a + ";\n\t\tЗначение 2 -", b + ".")
input()

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4
#Вычисление корней уравнения
from math import sqrt as q
print("Введите значения коэффициентов квадратного уравнения ax**2 + bx + c = 0")
a = int(input("\t\tЗначение a = "))
b = int(input("\t\tЗначение b = "))
c = int(input("\t\tЗначение c = "))
d = b**2 + ((-4) * a * c)
g = int(q(d))
x1 = (-b + g) / (2 * a)
x2 = (-b - g) / (2 * a)
x1 = str(x1)
x2 = str(x2)
print("\n\t\t\tX1 =", x1 + ";\n\t\t\tX2 =", x2 + ".")
input()
