
f = lambda n: n*f(n-1) if(n>0) else 1
print(f(5))
