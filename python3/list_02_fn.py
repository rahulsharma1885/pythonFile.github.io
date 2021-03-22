mylist = [3,4,5,23,67,7,77,6,8,9,0]
print(type(mylist))

mylist = [3,4,5,23,67,7,77,6,8,9,0]
mylist.remove(0)
print(mylist)

mylist = [3,4,5,23,67,7,77,6,8,9,0]
mylist.sort()
print(mylist)

mylist = [3,4,5,23,67,7,77,6,8,9,0]
mylist.append(99)
mylist.append(100)
print(mylist)

mylist = []
mylist.append(99)
print(mylist)

mylist = [3,4,5,23,67,7,77,6,8,9,0]  # last value ko remove kar dega
mylist.pop()
print(mylist)

mylist = [3,4,5,23,67,7,77,6,8,9,0]
mylist.insert(2,99)
print(mylist)