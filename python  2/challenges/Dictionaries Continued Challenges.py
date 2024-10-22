# How Many?
dictionary = {
	1: "bicycle",
	2: "soccer balls",
	3: "piano books"
}

dictionary[4] = input("What do you have 4 of?")
dictionary[5] = input("What do you have 5 of?")
dictionary[6] = input("What do you have 6 of?")
						  
print(dictionary)

# Work Schedule
work = {

	"Monday": 3,
	"Tuesday": 4, 
	"Wednesday": 2,
	"Thursday": 1, 
	"Friday": 1, 
	
}

work["Saturday"] = 5
work.pop("Wednesday")
print(len(work))

if "Friday" in work:
	print("Friday is in work")

print(work)