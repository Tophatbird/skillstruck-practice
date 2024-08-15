#What's the Century?
year = int(input("What year is it?"))

Century = int( year // 100 + 1 )
print(Century)
#florida divison :  x // y, this drops the decimal


#Debugging Challenge 2

#Find out how many people are coming to dinner
num_people = int(input("How many people are coming to dinner? "))
#You need to buy the food! Hamburgers are $1.29 each, rolls are $0.49, and corn is $0.80. Total up the items
hamburger_price = 1.29
rolls_price = 0.49
corn_price = 0.80

total_cost = hamburger_price + rolls_price + corn_price

hamburger_count = int(input("How many hamburgers will everyone have? "))

rolls_count = int(input("How many rolls will everyone have? "))

corn_count = int(input("How many pieces of corn will everyone have? "))


total = 0

total = total + (hamburger_count * hamburger_price * num_people)

total = total + (rolls_count * rolls_price * num_people)

total = total + (corn_count * corn_price * num_people)



noChange = int(total / num_people)

change = float(total / num_people)

print("Each person owes $" + str(noChange) + " without change, or $" + str(change) + " if change is included.")