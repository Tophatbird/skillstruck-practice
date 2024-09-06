# Last Minute Treats
first = input("What other item do you want?")
second = input("What final item do you want?")

treats = ["popcorn", "popsicles", "soda", "chips", "cookies"]

treats.append(first)
treats.append(second)

print(treats)

# Olympic Events

olympics = ["running", "gymnastics", "swimming", "volleyball", "basketball"]

new_olympics = ["karate", "surfing", "baseball", "skateboarding", "sport climbing"]

olympics.extend(new_olympics)

print(olympics)
