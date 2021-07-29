# Module - It is code library
# all ready some codes are in library so we have to use that one in our code
# inside mdule there is classes, objectives, modules, variables
'''
Types of module -
3 types of module - 
    1. custom module
    2. built in module
    3. external moule
'''

# custom module
import calculate
var = calculate.add1(4,6)
print(var)


from calculate import add1,sub1    # when we want only two function or there is no need of all function
var = add1(5,3)
print(var)

from calculate import add1,sub1    
var = mul1(5,3)                    # this mul1 will shows error because we didint impoted mul1
print(var)


from calculate import *             # * will import all the functions from calculate
var = div1(10,5)
print(var)


# built in  module
# go to command prompt and type help('modules') it will show all the modules which all ready exists in python
import math, calendar       # math and callendar are both buit in modules from python
var = math.factorial(5)
print(var)
var= calendar.TextCalendar().formatmonth(2020,12)
print(var)


# external module
from faker import faker

print(Faker().name())
print(Faker().email())
print(Faker().url())
