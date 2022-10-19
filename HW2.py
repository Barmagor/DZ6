#Задача из одного из семинаров

list1=["апар", "рплорлншгнш6", "hghghg", 4, "hgfffddss"]
ans=False
for i in list1:
    if isinstance(i, int):
        ans=True
        break
print(ans)

#2 cпособ
old_list = ['jhg', 'jh', 't', 5, 'hjgjg', 5, 6]
new_list = list(filter(lambda x: x if isinstance(x, int) else 0, old_list))
print (new_list)