#Reverse the number 
number = int(input("Pick a number that is two digits"))

last = number % 10
tens = number // 10

gog = str(last)
bob = str(tens)

reverse = (gog + bob)

print(reverse)

# Find the Ten's Place

num = int(input("enter a number thats 100 or greater"))

step_one = num % 100
step_two = step_one // 10
print(step_two)