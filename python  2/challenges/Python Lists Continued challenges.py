# Find the largest value

my_list = [int(n) for n in input().split()]
biggest_number = 0
for this_number in my_list:
	if this_number > biggest_number :
		biggest_number = this_number

print(biggest_number)


# Greater than left index

my_list = [int(n) for n in input().split()]

current = my_list[0]

for number in my_list :
	if number > current :
		print(number)
	current = number