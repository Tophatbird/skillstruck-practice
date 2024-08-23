# Same Color
x1 = int(input("enter the first digit"))
y1 = int(input("enter the second digit"))

x2 = int(input("enter the third digit"))
y2 = int(input("enter the fourth digit"))

color1 = (x1 + y1) % 2  # if 1 then black, if 0 then white
color2 = (x2 + y2) % 2  # if 1 then black, if 0 then white

if color1 == color2:
    print("Yes")
else:
    print("No")

# Leap Year
year = int(input("enter a year"))
if year % 4 == 0:
    print("Leap")
else:
    print("Common")