/* accomplish this task, you will need to use the 'random' module. The random module is one of Python's built-in modules. It has a choice method which returns a random item from a given sequence.

Step 1. Go to the first line of your file.

Step 2. Write import random on the line. Note: To import a module, you have to use the import keyword at the top of the file.

Step 3: Create the random.choice method and pass the word_list variable into the choice method.

Step 4: Assign the randomly generated word to a variable called word.

Step 5: Print out word to the standard output. Run the code several times and observe the words printed out after each run.
*/

import random 

word_list = ["Strawberries", "Blackberries", "Blueberries", "Grapes", "Mango"]

word = random.choice(word_list)

print(word)
