#if demo
sub1 = int(input("Enter Grade for subject 1: "))
sub2 = int(input("Enter Grade for subject 2: "))
sub3 = int(input("Enter Grade for subject 3: "))
sub4 = int(input("Enter Grade for subject 4: "))
sub5 = int(input("Enter Grade for subject 5: "))

average = (sub1 + sub2 + sub3 + sub4 + sub5) / 5
print("your average grade is {average} ")
if average >= 90:
    print("you are excellent!")
elif average >= 70:
    print("you passed!")
    print("Congratulations!")
else:
    print("you are failed")