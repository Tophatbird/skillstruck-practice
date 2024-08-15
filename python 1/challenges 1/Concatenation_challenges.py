#Halloween Candy Count
snickers = int(input("How many snickers did you get?"))
nerds = int(input("How many nerds did you get?"))
butterfingers = int(input("How many butterfingers did you get?"))

one = str(snickers)
two = str(nerds)
three = str(butterfingers)

total = snickers + nerds + butterfingers
toe = str(total)

print("This year, you got " + one + " snickers, " + two + " nerds, and " + three + " butterfingers. The total number of these candies is " + toe + " candies.")

#Detective Buggy's Message

recipient = input('Who is the message for?')

place = input('Where do you want to meet?')

minutes = input('In how many minutes would you like to meet?')

print("I have an important message for " + recipient + ". Meet me at the " + place + " in " + minutes + " minutes. From, Detective Buggy." )