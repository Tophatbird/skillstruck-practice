# Secret Beach Day
amanda_value = int(input("How many in Amanda's group?"))
jane_value = int(input("How many in Jane's group?"))

group = {
	"Fred" : 12,
	"Jackson" : 15,
	"Sophie" : 20,
	"Amanda" : amanda_value,
	"Jane" : jane_value,
}

total = 0

for attendes in group.values():total += attendes
	
print(total)

# Shoes
name = input("What is another name?")
shoes =int(input("How many shoes does " + name + " have?"))
group = {
	"Sally" : 10,
	"Cameron" : 3,
	"Spencer" : 6,
	name : shoes,
}

group_num = 0
for child , amount in group.items():
	print( child + " has " + str(amount) + " pairs of shoes.")