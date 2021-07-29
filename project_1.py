import random

def game_win(comp, you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True

print("Comp turn: Snake(s) Water(w) anf Gun(g)")
rand_no = random.randint(1,3)
if rand_no == 1:
    comp = 's'
if rand_no == 2:
    comp = 'w'
if rand_no == 3:
    comp = 'g'

you = input("Your turn: Snake(s) Water(w) anf Gun(g)")
a = game_win(comp, you)

print(f"Computer choose{comp}")
print(f"Your turn {you}")

if a == None:
    print("tie!!")
elif a:
    print("you win")
else:
    print("you loose")
