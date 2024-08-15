#the character count starts at 0 and spaces count count as characters

string1 = "peepee poopoo man"

print(string1[8:10])
#this will only print the characters between those characters 

print(string1.split())
# this will seprate the words

print(len(string1))
#this will tell you how many characters there are

print(string1.find("m"))
#this finds the first instance of the letter from the start to last.
#to find the letter from back to front  you need something like this: string1.rfind()