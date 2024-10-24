num = int(input("write your number "))
for i in range(2,num//2):
    if num%i == 0:
        print("your number is not prime")
        exit()
print("your number is prime")