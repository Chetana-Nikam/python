a = int(input("Enter 1 no "))
b = int(input("Enter 2 no "))
c = int(input("Enter 3 no "))
d = int(input("Enter 4 no "))
if(a>b and a>c and a>d):
    print("Greater no is: ", a)
elif(b>a and b>c and b>d):
    print("Greater no is: ", b)
elif(c>a and c>b and c>d):
    print("Greater no is: ", c)
else:
    print("Greater no is: ", d)


