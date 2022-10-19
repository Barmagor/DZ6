#3 задача из второго дз
#сразу улучшенная версия
##def formula(i):
    ##return lambda i:pow((1/i+1),i)
x=lambda i:pow((1/i+1),i)

n = int(input("Введите число: "))
for i in range (n+1):
    if i !=0:
        print(x(i), end=" ")
y=0
for j in range (n+1):
    if j !=0:
        y=x(i)+y
print("Сумма =", y)