def sum(n):
    if n == 1:
        return 1
    if n==0:
        return 0
    else:
        return n + sum(n-1)
c = sum(4)
print(f"Sum is {c}")