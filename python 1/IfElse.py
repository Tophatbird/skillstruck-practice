coins = 10
money = int(input("How many coins do you have?"))
if coins < money:
     print("You have more than enough to buy a puppy.")
elif coins == money : 
     print("You have exactly enough to buy a puppy.")
else:
      print("you do not have enough to buy a puppy.")