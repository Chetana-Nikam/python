# File Handling
# File saved by .txt then it is text file
# File saved by .xls then it is exel file
'''
syntax
open('file_path', 'mods')

There is 5 types of mod
x -creat file    
r -read file
a -append file  - it will creat file if it is not available
w -write file
r+ -read/write file
'''

f1 = open('demo.txt', 'x')

f1 = open('demo.txt', 'r')
print(f1.read())

f1 = open('demo.txt','w')
f1.write('\n hgfhgbjnklmlm545151')
f1.close()

with open('demo.txt','w') as f1:
    f1.write('sdghjbfbjbmmn')

f1=open('demo.txt','r+')
print(f1.read())
f1.write('12345678910')
f1.close()

# how to delete file
# os is a built in module of python
import os
print(os.getcwd())
os.mkdir('newfolder')




