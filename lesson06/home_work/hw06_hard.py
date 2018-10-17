# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла

#Функция создания файла расчетной ведомости
def create_files(name, surname, work_hours):
	n = open(name + "_" + surname + ".txt", "w")
	n.write(name + " " + surname + " " + work_hours)
	n.close()
#Функция чтения файла расчетной ведомости
def read_files(file_name):
	n = open(file_name, "r")
	aa = n.read()
	n.close()
	return aa
#Создаю файлы расчетной ведомости
a = create_files("Abraham", "Smith", "90")
b = create_files("Jim", "Kerri", "100")
c = create_files("Anatolii", "Zvezdochkin", "250")
#Читаю эти файлы, после монипуляций присваиваю и сортирую содержимое файлов в переменные
ab = read_files("Abraham_Smith.txt")
worker1 = tuple(ab.split(" "))
name1 = worker1[0]
surname1 = worker1[1]
hours1 = worker1[2]
av = read_files("Jim_Kerri.txt")
worker2 = tuple(av.split(" ")) 
name2 = worker2[0]
surname2 = worker2[1]
hours2 = worker2[2]
ac = read_files("Anatolii_Zvezdochkin.txt")
worker3 = tuple(ac.split(" "))
name3 = worker3[0]
surname3 = worker3[1]
hours3 = worker3[2]
print("Расчет заработной платы работников за месяц: Норма - 100ч. ; З/П - 150 000$")
#Пишу класс расчета заработной платы сотрудников и Анатолия
class Workers:
	def __init__(self, name, surname, hours):
		self.name = name
		self.surname = surname
		self.hours = hours
	def zp(self, name, surname, hours):
		if int(self.hours) == 100:
			print("\nСотрудник {} {} отработал необходимую норму часов(100ч)\
				\nего заработная плата составляет 150 000$" .format(self.name, self.surname))
		elif int(self.hours) < 100:
			a = 150000 / 100
			b = 100 - int(self.hours)
			money = 150000 - a * b
			print("\nСотрудник {} {} не отработал необходимую норму часов({} < 100ч)\
				\nего заработная плата составляет {}$" .format(self.name, self.surname, self.hours, str(money)))
		elif int(self.hours) > 100 or self.name == "Anatolii":
			a = 150000 / 100
			b = int(self.hours) - 100
			money = 150000 + a * b * 2
			print("\nСотрудник {} {} отработал больше необходимой нормы часов({} > 100ч)\
				\nего заработная плата составляет {}$" .format(self.name, self.surname, self.hours, str(money)))
#Далее обращаюсь к классу и получаю расчет заработной платы рабочих и Анатолия
worker1 = Workers(name1, surname1, hours1)
worker2 = Workers(name2, surname2, hours2)
worker3 = Workers(name3, surname3, hours3)
worker1.zp(name1, surname1, hours1)
worker2.zp(name2, surname2, hours2)
worker3.zp(name3, surname3, hours3)
