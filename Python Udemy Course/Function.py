# function -  It is block of code and it will work only when we call it
def myfun():
    print("I am Function")
myfun()                      # Function call




def myfun(name, age):
    print(f"My name is {name} and my age is {age}")
myfun('Chetana', 21)
myfun('Google', 20)



def myfun(*name):           # * indicats arbitary argument
    print(f"My name is {name[1]}")
myfun('Chetana', 'Manisha', 'Prakash')



# def myfun(name):
#     print(f"My name is {name}")
# myfun()                              # if we didnt pass anything when function is calling then it will gives error so we have to pass one default value in function



def myfun(name='Chetana'):
    print(f"My name is {name}")
myfun()


def myfun(name):
    for i in name:
        print(i)
name=('Chetana', 'Manisha', 'Prakash')
myfun(name)





def myfun(x):
    return x*x
print(myfun(8))
print(myfun(5))
