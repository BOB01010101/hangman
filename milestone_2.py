import random 

word_list = ["Strawberries", "Blackberries", "Blueberries", "Grapes", "Mango"]

word = random.choice(word_list)

print(word)

guess = input("Enter a single letter")

if ( len(guess) == 1 and type(guess) == str):
  print("Good guess!")
else:
  print("Oops! That is not a valid input.")


