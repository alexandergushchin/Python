# Задание 2
a = int(input("Введите количество секунд: "))
h = a // 3600
m = a % 3600 // 60
# Либо так:
#m = (a - h * 3600) // 60
s = a % 3600 % 60
# Либо так:
#s = a - h * 3600 - m * 60
print("Такое количество секунд в формате ЧЧ:ММ:СС равно:", (f'{h:02d}:{m:02d}:{s:02d}'))

#Особенности форматирования f-строк пока не усвоил.