f = open("ab.txt")

f.seek(4)
print(f.tell())
print(f.readline())
print(f.readline())
f.close()