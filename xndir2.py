text = input("write any sentence ")
shyochik = 0
for i in range(0,len(text)):
    if text[i] in ['a','e','i','o','u']:
        shyochik +=1
print(shyochik)