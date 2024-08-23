#Cookie Cost Calculator
dollars = int(input("How many dollars does a cookie cost?"))
cents = int(input("How many cents is in the cost?"))
amount = int(input("How many cookies would you like to buy?"))

cookies = dollars + cents /100

cost = cookies * amount
total = str(cost)

message = "The total cost of {} cookies is ${}"

print(message.format(amount, total))

#Sum the digits
number = input("Enter a number with three digits")
(number.split())

first = number[0]
second = number[1]
third = number[2]

total = int(first) + int(second) + int(third)

sum = "The sum of those digits is {}"
print(sum.format(total))