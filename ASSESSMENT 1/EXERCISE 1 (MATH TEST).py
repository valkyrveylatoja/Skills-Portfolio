"""
EXERCISE 1 - Math Quiz by Val Kyrvey Latoja

Important functions:

displaymenu
randomint
decideoperation
displayproblem
iscorrect
displayresults
"""
# importing modules
import random
from time import time
from random import randint

start_time = time() # calculating the amount of time of answering the whole quiz

def displaymenu(): # function for difficulty selection
    print("----- All Difficulties -----")
    
    print("1.) Easy")
    print("2.) Moderate")
    print("3.) Advanced")

def selectdifficulty(difficulty): # no. of digits dermined of each desired difficulty
    if difficulty == 1:
        return random.randint (0,9)
    elif difficulty == 2:
        return random.randint (0,99)
    elif difficulty == 3:
        return random.randint (0,999)

def decideoperation(): # randomizing between subtraction and addition
    return random.choice(['+', '-'])

def displayproblem(no1,no2,operator): #  displays a question depending on the decideoperation()
    return f"What is {no1} {operator} {no2} = "

def displayresults(points): # displays results
    elapsed_time = time() - start_time
    print(f"----- Your score is {points}/100. Elapsed Time: {elapsed_time:.2f} seconds. -----")

    if points <= 59:
        print("----------------------- Grade: F ------------------------------")
    elif points <= 69:
        print("----------------------- Grade: D ------------------------------")
    elif points <= 79:
        print("----------------------- Grade: C ------------------------------")
    elif points <= 89:
        print("----------------------- Grade: B ------------------------------")
    elif points <= 100:
        print("----------------------- Grade: A ------------------------------")

def quiz(): # initiates the entirity of functions
    displaymenu()
    points = 0

    try:
        difficulty= int(input("Select a Difficulty: ")) # determinant for selectdifficulty()
        if difficulty > 3 or difficulty < 1:
            print("xxxxx Not a valid option. xxxxx")
            return
    except ValueError:
        print("xxxxx Not a valid option. xxxxx")
        return

    for _ in range (10): #limiting to only 10 questions
        no1 = selectdifficulty(difficulty)
        no2 = selectdifficulty(difficulty)
        operator = decideoperation()

        if operator == '+':
            answer1 = no1 + no2
        
        if operator == '-':
            answer1 = no1 - no2

        start_time = time() # calculating the amount of time to answer each question

        try:
            problem = displayproblem(no1, no2, operator)
            answer2 = int(input(problem))
            elapsed_time = time() - start_time
            
            if answer1 == answer2:
                points += 10
                print(f'^^^^^ Correct! Answered in {elapsed_time:.2f} seconds. ^^^^^')
            
            else:
                print(f'vvvvv Wrong! Answered in {elapsed_time:.2f} seconds. vvvvv')
        
        except ValueError:
            print("xxxxx That is not a number. xxxxx")

    displayresults(points)

while True: # if true this will activate and prevents indefinite repetition
    quiz()