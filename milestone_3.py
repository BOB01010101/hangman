"""while (True):
  
  guess = input("Guess a letter from the alphabet")
  if (len(guess) == 1 and guess.isalpha() == True):
    break
  else:
    print("Invalid letter. Please, enter a single alphabetical character.")
"""

from random_word import RandomWords

"""random_words = RandomWords()
print(random_words.get_random_word())

if guess in random_words.get_random_word(): 
  print(f'Good guess! {guess} is in the word.')
else:
  print(f"Sorry, {guess} is not in the word. Try again.")

"""
  
guess = input("Guess a letter from the alphabet")

def check_guess(guess): 
  guess.lower()
  if guess in random_words.get_random_word(): 
   print(f'Good guess! {guess} is in the word.')
  else:
   print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input():
    while (True):
     if (len(guess) == 1 and guess.isalpha() == True):
      break
     else:
      print("Invalid letter. Please, enter a single alphabetical character.")
check_guess(guess)
  
ask_for_input()





