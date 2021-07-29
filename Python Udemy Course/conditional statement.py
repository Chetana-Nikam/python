#conditional statement
'''
if        agar
elif      ya fir
else      nahi toh
'''

a=11
b=55
if b<a:
    print("b is bigger")
else:
    print("a is bigger")



p=10
q=10
if p<q:
    print("q is bigger")
elif p>q:
    print("p is bigger")
elif p==q:
    print("Both are equal")
else:
    print("Somethingis wrong")



x=10
y=10
if x<y:
    print("y is bigger")
elif x>y:
    print("x is bigger")
else:
    print("Both are equal")


# Short hand program of if elif else

a,b=55,11
if a==b: print("a is bigger")

a,b=11,55
print("b is bigger") if b>a else print("a is bigger")




# Logical Operator
a,b,c=55,11,23
if a>b and c>a and a != b:
    print("all conditions are true")
else:
    print("false condition")

# Nested if     
num=12
if num >= 0:
    if num==0:
        print("zero")
    else:
        print("num is positive")
else:
    print("num is negative")