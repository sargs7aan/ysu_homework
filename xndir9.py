N = int(input("how many types of products you have? "))
product = []
price = []
tot = 0
for i in range(0,N):
    print("enter product ")
    product.append(input())
    print("enter price of entered product ")
    price.append(int(input()))
dict = {}
for i in range(0,N):
    dict[product[i]] = price[i]
for i in range(0,N):
    tot +=price[i]
print(dict)
print(tot)
