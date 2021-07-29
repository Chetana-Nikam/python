# a = input("Enter first number: ")
# b = input("Enter second number: ")
# avg = (a + b)/2
# print("The average of a and b is", avg)
# This program will gives error because type of a and b is string we cannot do avg of string



a = input("Enter first number: ")
b = input("Enter second number: ")
a = int(a)
b = int(b)
avg = (a + b)/2
print("The average of a and b is", avg)

