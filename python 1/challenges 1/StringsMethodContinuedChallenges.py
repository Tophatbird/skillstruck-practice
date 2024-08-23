#Remove String Section
noj = input("write a sentence with two 'j's.")

firstj = noj.find('j')
secondj = noj.rfind('j')

nomore = noj[:firstj] + noj[secondj + 1:]

print(nomore)

Reverse String Section

user = input("write a sentence with two 'j's.")

firstj = user.find('j')
secondj = user.rfind('j')

reverse = user[firstj] + user[secondj + 1:]

print(reverse)


user = input("write a sentence with two 'g's.")
second_g = user.rfind('g')
print(second_g)