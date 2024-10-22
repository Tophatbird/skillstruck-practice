# Check for key
dictionary = {
  7: "first", 
  3: "second", 
  4: "third", 
  8: "fourth", 
  9: "fifth", 
}

my_list = [int(n) for n in input().split()]

for key in my_list :
    if key in dictionary : print("Yes")
    else: print("No")

#Power dictionary

n = int(input("How many keys in dictionary?"))

dictionary = {}

for number in range(n):
    dictionary[number] = number * number

print(dictionary)