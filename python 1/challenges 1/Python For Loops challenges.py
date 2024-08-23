# Add the Numbers
number_one = int(input("enter a number"))
number_two = int(input("enter a number"))

if number_one > number_two:
    number_one, number_two = number_two, number_one

total = 0

for x in range(number_one, number_two + 1):
  total += x
  
print(total)