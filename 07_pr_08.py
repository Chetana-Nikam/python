n=3
for i in range(3):
    if i == 0:
        print("*" * 3)
    if(i == 1):
        print("*" * i, end="")
        print(" " * i, end="")
        print("*" * i)
    if(i == 2):
        print("*" * 3)