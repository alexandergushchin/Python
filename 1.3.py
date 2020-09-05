# Задание 3
n = int(input("Введите натуральное число: "))
step = 10
while n // step > 0:
    step = step * 10
x = n + step * n + n + step ** 2 * n + step * n + n
print("n + nn + nnn =", x)


