sub1 = int(input("enter 1 subject marks: "))
sub2 = int(input("enter 2 subject marks: "))
sub3 = int(input("enter 3 subject marks: "))
if(sub1<33 or sub2<33 or sub3<33):
    print("You are fail")
if((sub1 + sub2 + sub3)/3 < 40):
    print("You r fail because u have less than 40")
else:
    print("Congratulations... You passed exam")