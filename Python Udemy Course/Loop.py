#Loop
print("Chetana "*20)

# For Loop
num=[1,2,3,'Chetana']    #List
for i in num:
    print(i)

#Range
# range(start, end, difference)
for i in range(11):                  # 11 is end point here we didnt give starting point therefor by default it ts 0 and difference is by default 1
    print(i)

for a in range(1,20,2):
    print(a)


#break - it breaks the loop and exit from loop
for q in range(8):
    if q == 4:
        break
    print(q)


#continue 
for e in range(8):
    if e==4:
        continue
    print(e)


# Nested loop
name=['chetana', 'susmita', 'yash']
surname=['Nikam', 'patil', 'khilare']
for i in name:
    for a in surname:
        print(i,a)
        



        


 