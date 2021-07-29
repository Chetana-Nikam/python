#While Loop

#i=0
#while i<5:
#    print(i)     # infinite times loop will exist because i=0 always less than 5


i=0
while i<5:
    print(i)
    i += 1



i=0
while i<=10:
    i += 1
    if i==6:
        break
    print(i)


i=0
while i<=10:
    i += 1
    if i==6:
        continue
    print(i)
    