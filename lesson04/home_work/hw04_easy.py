# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]
import random
list1 = []
list2 = []
for i in range(random.randint(50, 100)):
	list1.append(random.randint(1, 100))
for i in list1:
	list2.append(i ** 2)
# Задание-2:import random
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.
import random
fruits = ["абрикос", "черешня", "вишня", "банан", "слива", "яблоко"]
list1 = []
list2 = []
list3 = []
for i in range(5):
	a = random.randint(0, len(fruits) -1)
	b = random.randint(0, len(fruits) -1)
	list1.append(fruits[a])
	list2.append(fruits[b])
for i in list1:
	if i in list2:
		list3.append(i)
print(list1)
print(list2)
print(list3)
# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4
import random
list1 = []
list2 = []
for i in range(random.randint(50, 100)):
	list1.append(random.randint(1, 100))
for i in list1:
	if i % 3 == 0 and i > 0 and i % 4 != 0:
		list2.append(i)
print(list1)
print(list2)
