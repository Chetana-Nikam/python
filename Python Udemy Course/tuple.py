# Tuples
t1=(2,45,2.5,'Hii','Chetana')   # tuples are in () brackets
print(t1)
print(len(t1))
print(type(t1))
print(t1[2])
print(t1[-1])
print(t1[2:4])
print(t1[:5])
#print(t1.append("nikam"))    # it will shows erroe because we cannot add remove data in tuples but one way to do this is convert tuples into list
l1=list(t1)                  # t1 in converted into list
print(l1)
print(type(l1))
l1[1]='ss'
t1=tuple(l1)
print(t1)
t2=('a','f',25,0)
x=t1 + t2
print(x)




