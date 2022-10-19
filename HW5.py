# Найти сумму четных чисел от N до нуля с помощью цикла while
num1 = int(input("Введите число: "))
i=0
sum1=0
while i <= num1:
    if i%2 ==0:
        sum1=i+sum1
    i+=1
print(sum1)

#2 способ, по смыслу мэп здесь не нужен, но я его потренировал
lst=[]
for i in range(num1):
    lst.append(i)
res=list(filter(lambda i:i%2==0, lst))
print(res)
res2=list(map(lambda i:i+i, res))
print(res2)
print(sum(lst))