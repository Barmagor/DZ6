#Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
import random
print("Введите число N")
n=int(input())
for i in range(n):
    c=random.randint(0, 10)
    print(c, end=" ")

#2 способ с подсчётом количества рандомов от нуля
print("Введите число N")
n=int(input())
my_list=[random.randint(0, 10) for i in range(n)]
print(list(enumerate(my_list)))
    