# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    number = str(number)
    g = number.split(".")
    #Создаю строки отрезков итогового числа
    #1 - целая часть
    #2 - дробная часть без округляемого числа
    #3 - монипуляции с округляемым числом
    
    #1
    a = g[0]
    
    #2
    v = g[1]
    o = v[0:ndigits - 2]
    ff = v[0:ndigits]

    #3
    b = v[ndigits - 1]
    t = v[ndigits]
    #Создаю число типа float, (не математически) округляя его
    hpp = a + "." + ff
    hpp = float(hpp)
    #Создаю число типа float, на каторое буду увеличивать исходное при округлении
    kk = "0." + "0" * (ndigits - 1) + "1"
    kk = float(kk)
    #условие математического округления
    if int(t) >= 5:
    	hpp += kk
    return hpp
print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    number = str(ticket_number)
    #Проверяю, правильно ли введен шестизначный билет
    if len(number) != 6:
        return "Неправильный номер билета!"
    #Проверяю, равна ли сумма 2х первых чисел 2ум последним
    if int(number[0]) + int(number[1]) == int(number[4]) + int(number[5]):
        return "Счастливый билет!"
    #Проверяю, равна ли сумма 3х первых чисел 3ем последним
    elif int(number[0]) + int(number[1]) + int(number[2]) == int(number[3]) + int(number[4]) + int(number[5]):
        return "Счастливый билет!"
    else:
        return "Билет не счастливый!"
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
