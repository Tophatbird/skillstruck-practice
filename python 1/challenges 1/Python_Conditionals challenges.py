# #More than average?
number = int(input("enter a number"))
if number > 50:
    print("More than average")
elif number < 50:
    print("Fewer than average")
else:
    print("The average")
# Black Square
coord = int(input("enter the first digit"))
inates = int(input("enter the second digit"))
add = coord + inates
if add % 2 == 1:
    print("Yes")
else:
    print("No")