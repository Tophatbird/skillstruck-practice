number = int(input("How many employees?"))

tables = 0
if number % 2 == 0: #there is an even number of employees
    tables =  number // 2
else: # there is an odd number of employees
    tables =  number // 2 + 1


minimum = "Minimum number of tables: {}"



print(minimum.format(tables))

jasbags = int(input("Jasmine has bags that can hold 12 marbles each and Chloe has bags that can hold 10 marbles each, how many bags will Jasmine have?"))

chlbags = int(input("How many bags will Chloe have?"))

jasmarbles = jasbags * 12
chlmarbles = chlbags * 10

string1 = "If Jasmine had {} bags, she would have {} marbles total. If Chloe had {} bags, she would have {} marbles total."
print(string1.format(jasbags, jasmarbles, chlbags, chlmarbles))