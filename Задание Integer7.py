import math
print('Введите двузначное число: ')
A = int(input())
summa = (A // 10) + math.fmod(A, 10)
print('Сумма его цифр равна: ', int(summa))
proiz = (A // 10) * math.fmod(A, 10)
print('Произведение его цифр равно: ', int(proiz))
