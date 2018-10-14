# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


#Вот код соответствующий всем требованиям:
import os
from shutil import copyfile as copy
def create():
	a = 1
	while True:
		if a == 10:
			break
		dir_path = os.path.join(os.getcwd(), "dir_" + str(a))
		try:
			os.mkdir(dir_path)
		except Exception:
			print("Файл уже сущуствует!")
		a += 1
	print("Успешно!")
def delite():
	a = 1
	while True:
		if a == 10:
			break
		dir_path = os.path.join(os.getcwd(), "dir_" + str(a))
		try:
			os.rmdir(dir_path)
		except Exception:
			print("Файл не сущуствует!")
		a += 1
	print("Успешно!")
def papk():
	print("Все папки текущей директории:")
	list = os.listdir()
	papki = []
	for i in list:
		if os.path.isdir(i):
			papki.append(i)
	return papki
def file():
	name = os.path.abspath(__file__)
	copy(name, "copy")
	print("Успешно!")

while True:
	print("1 - Создать 9 файлов")
	print("2 - Удалить созданные 9 файлов")
	print("3 - Просмотреть папки текущей директории")
	print("4 - Скопировать текущий файл")
	print("5 - Выход")
	ans = input("\t")
	if ans == "5":
		break
	elif ans == "1":
		print(create())
	elif ans == "2":
		delite()
	elif ans == "3":
		print(papk())
	elif ans == "4":
		file()
	else:
		print("Неверный ответ!")
