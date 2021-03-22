num = int(input("enter the year \n"))
for i in range(2,num):
    if(num%i == 0):
        break
        print("not prime")
    else:
        print("prime")