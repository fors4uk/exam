print("Введите число")
n = int(input())
k = 2
summa = 0

while n > 0:
        if k < 1:
            break
        summa = summa + n%10
        k = k-1
        n = n // 10
 
print("Сумма цифр:", summa)

