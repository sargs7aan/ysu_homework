length = int(input("tell the length of list that u want to create "))
list = []
for i in range(0,length):
    list.append(input())
max = list[0]
for i in range(0,length):
    if list[i] >= max:
        max = list[i]
print(max)
