#set  - denoted by{} - set is unordered and unindexed 
s1={'abc',5,25.26,'nikam'}
print(s1)
# in set we can enter duplicate items means we cannot write item 2 or 3 times
s2={'abc',2,2,2,5,8,9}
print(s2)                 # 2 printed only ones
print(len(s2))
print(type(s2))
# we cannot access items of set
# we can access by converting set into tuple or list
s1.add('red')   # we can add item
print(s1)
s1.remove('abc')  # we can remove item by defining item itself because set doesnt have index values
print(s1)
s1.discard('nikam')
print(s1)
x= s1.union(s2)
print(x)
s3= {1,2,3}
s4= {4,5,6}
s3.update(s4)   # other way to merg two sets
print(s3)



