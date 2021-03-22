def  nextprime(n):
    while(n):
        n = n+1
        for i in range(2,n):
            if(n%i==0):
                break
            else:
                return n
nextprime(3)