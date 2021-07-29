# Lambda function - we can perform or define our task in one line
'''
Syntax
    lambda arguments : expression
'''

def xyz(a,b,c):
    return a*a+2*b/c
print(xyz(3,4,8))

# now with the help of lambda
xyz = lambda a,b,c : a*a+2*b/c
print(xyz(3,4,8))

# map function
'''
syntax
   map(function, iterables)
'''
l1=[5,6,7]
l2=[6,10,2]
xyz=lambda n,m : n*m
l3=map(xyz,l1,l2)
print(list(l3))

# Filter function 
'''
syntax
   filter(function, iterable)
'''
l=[4,7,3,9,8,2,0,1]
def even(n):
    if n%2==0:
        return True
    else:
        return False
result = filter(even, l)
print(list(result))
