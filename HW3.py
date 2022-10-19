# 1 Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
list1 = []
for i in range (0, 11):
    list1.append(i)
print(list1)
sum1 = 0
for i in list1:
    if i%2 !=0:
        sum1=i+sum1
    i+=1
print(sum1)

#2 cпособ
list2=[j for j in range(0, 11)]
print(list2)
res=list(filter(lambda i:i%2>0, list2))
print(res)
print(sum(res))

