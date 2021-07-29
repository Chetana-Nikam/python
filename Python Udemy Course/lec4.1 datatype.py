#list

l1=[1,5,96,1,6.3,'Chetana']
print(l1)
print(len(l1))
print(l1[0])        #for accesing data from list
print(l1[4])
print(type(l1))
print(l1[-1])       #for accessing data in reverse order
print(l1[2:5])
print(l1[:5])
print(l1[5:])
l1[3]='ss'          #changing data from list
print(l1)
l1.insert(2,49.50)   # for adding new value 2 is index value and 49.50 is the value which we are going to insert
print(l1)
l1.append("my append")   # by default it will goes at the end of list
print(l1)
l1.remove(6.3)           # for removing data from list by puting value itself
print(l1)
l1.pop(4)                # removing data through index
print(l1)
l1.pop()                 # now it will remove last value or data
print(l1)
del l1[4]                # another way to delete data from list by defining index number
print(l1)
l2=[2,5,6,9,7]        
l2.sort()                # sorting
print(l2)
l3=['h','a','d','r','c']
l3.sort()
print(l3)
l3.sort(reverse=True)    #for reverse sorting
print(l3)
l2.sort(reverse=True)
print(l2)
x=l1 + l2 + l3
print(x)