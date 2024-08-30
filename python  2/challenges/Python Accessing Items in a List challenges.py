#Multiply Center Number
# my_list = [int(n) for n in input("Create a list of 9 numbers").split()]

# middle = my_list[4]

# result = middle * 100

# print(result)

my_list = [int(n) for n in input("Input a list of numbers").split()]

for number in my_list:
    if number + 1 not in my_list:
      print(number + 1)
