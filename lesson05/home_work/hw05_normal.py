# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py


#Вот код файла module.py:
def cr(x):
	import os
	dir_path = os.path.join(os.getcwd(), x)
	try:
		os.mkdir(dir_path)
	except Exception:
		print("\aФайл уже сущуствует!")
	print("Успешно создано!")
def dl(x):
	import os
	dir_path = os.path.join(os.getcwd(), x)
	try:
		os.rmdir(dir_path)
	except Exception:
		print("\aФайл не сущуствует!")
	print("Успешно удалено!")
def cod():
	import os
	return os.listdir()
def soder(x):
	import os
	try:
		return os.listdir(x)
	except Exception:
		print("\aНеверный путь!")

#Теперь сам код:
import module
answer = None
while True:
	print("Выберите действие:")
	print("\t\t1 - Просмотреть содержимое папки")
	print("\t\t2 - Просмотреть содержимое текущей папки")
	print("\t\t3 - Удалить папку")
	print("\t\t4 - Создать папку")
	print("\t\t5 - Выход")
	answer = input("\t")
	if answer == "5":
		print("\n\t\t\tДо свидания!")
		break
	elif answer == "1":
		name = input("Введите полный путь к папке для ее просмотра:\n\t")
		module.soder(name)
	elif answer == "2":
		print("Вот содержимое текущей папки:")
		print(module.cod())
	elif answer == "3":
		name = input("Введите название папки для удаления:\n\t\t")
		module.dl(name)
	elif answer == "4":
		name = input("Введите название новой папки:\n\t\t")
		module.cr(name)
	else:
		print("\aНеверный ввод данных! Повторите повытку снова!")
