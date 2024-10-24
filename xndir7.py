len = int(input("write the length of list"))
list = []
sorted_list = []
for i in range(0,len):
    a = int(input())
    list.append(a)
for i in range(0,len):
    if list[i]%2==1:
        sorted_list.append(list[i])
print(sorted_list)