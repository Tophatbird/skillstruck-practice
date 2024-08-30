# Count the zeros
my_list = [int(n) for n in input("Input a list of numbers").split()]

amount = 0	
for x in my_list:
    if x == 0:
        amount += 1

print(amount)
# Color Inspector

choice = input("Choose a letter")

my_list = ["red", "orange", "yellow", "green", "blue", "purple", "black", "white", "gray", "pink", "indigo", "brown", "tan", "gold", "silver"]

totol = 0

for x in my_list:
	if choice in x:
		totol += 1 
		
total = str(totol)

print("There are " + total + " items in the list that have the letter " + choice + " in it.")