"""
EXERCISE 2 - Alexa tell me a joke by Val Kyrvey Latoja
"""

import random # importing the random module

# function for reading each joke line
def loadmyjokes(joke_filepath): # the function will derive from a context manager
    with open(joke_filepath, 'r') as jokefile: # opens the text file. 'r' is a command that will only read the file and nothing else.
        jokes = jokefile.readlines() # reads all the lines within the the text file
    return [joke.strip() for joke in jokes] # ends the function using a list comprehension. .strip() separates a joke line from whitespaces.

def tellmeajoke(jokes):
    return random.choice(jokes) # selects a random, element from the jokes list.

# a recap of every function and use them in this function
def main():
    jokes = loadmyjokes('randomJokes.txt') # uses the loadmyjokes() function from the specified file

    while True: # loops whenever the user inputs an invalid answer
        prompt = input('Prompt: ').strip() # using a prompt variable for the if statement below.

        if prompt.lower() == "alexa tell me a joke": # prompt.lower() converts the prompt into lower case; no matter what you capitalized. this is to accept the prompt in mixed cases
            print(tellmeajoke(jokes)) # prints the tellmeajoke()

        else: # if the user types in an invalid prompt
            print("Invalid Prompt. Try again.")
            continue # skip to the next interation of the loop if the prompt is incorrect

        while True: # loops whenever someone answers an invalid option
            again = input("Do you want to hear another joke? (yes/no): ").strip().lower() # .strip() and .lower() to trim the input into its expected output
            if again in ["yes","no"]: # cheking if the user only answers these options
                    break # breaks the loop if the answer is valid
            print("Please answer 'yes' or 'no'.")  # if the answer is invalid it moves on to the next line which is this one
        
        if again == "no": # if user doesnt want another joke this loop breaks
            break

main() # run the main() function