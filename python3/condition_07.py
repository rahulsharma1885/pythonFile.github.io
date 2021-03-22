sub1 = int(input("enter the first subject number \n"))
sub2 = int(input("enter the second subject number \n"))
sub3 = int(input("enter the third subject number \n"))
if(sub1<33 or sub2<33 or sub3<33):
    print("you are fail")
elif(sub1+sub2+sub3)/3 < 40:
    print("you are fail because your average marks less than 40")
else:
    print("passed")