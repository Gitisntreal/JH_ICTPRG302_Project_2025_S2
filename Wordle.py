# Assessment Task 3 (AT3): Project
#
# Author: Jason Huynh
# Student ID: 20134959
#
# Course: ICT40120 (Data Science and AI)
# Lecturer: Chris

# TODO: Add Import statements (if needed)

# Variables and Constants
# TODO: Define Constants

# TODO: Define Variables 

# Application Functions
# TODO: Score Guess Function
# Jason Huynh 20134959 - 5/11/2025
def score_guess(guess, target):
    score = [0] * len(target)
    target_letter = list(target)
    for i in range(len(target)):
        if guess[i] == target[i]:
            score[i] = 2
            target_letter[i] = None
    for i in range(len(target)):
        if score[i] == 0 and guess[i] in target_letter:
            score[i] = 1
            target_letter[target_letter.index(guess[i])] = None
    return score

# Test Case 1
## Arrange 
guess_word = 'hello'
target_word = 'train'
## Act
score = score_guess(guess_word, target_word)
## Assert
print('Score:', score, 'Expected:', [0, 0, 0, 0, 0])

# Test Case 2
## Arrange 
guess_word = 'hello'
target_word = 'hello'
## Act
score = score_guess(guess_word, target_word)
## Assert
print('Score:', score, 'Expected:', [2, 2, 2, 2, 2])

# Test Case 3
## Arrange 
# TODO: set guess word to "world"
guess_word = 'world'
# TODO: set target word to "hello"
target_word = 'hello'
## Act
# TODO:  set score to score guess (guess word and target word)
score = score_guess(guess_word, target_word)
## Assert
# TODO: display the score
print('Score:', score, 'Expected:', [2, 2, 2, 2, 2])


# Pseudocode - defining an algorithm for scoring
"""
Start:
    Get Guess and Target Words
    Initialise Score as a list of 0s of length of Target Word
    For position in length of Target Word:
        If letter at position in Guess word equals letter at position in Target word:
            Set score at position to 2
        :End if
    :End for
    For position in length of Target Word:
    if score at position not equal to 2:
        if letter at position in Guess is in Target Word and Target Word count of that letter is greater than number of times letter has already been scored as 2 or 1:
            set score at position to 1
        End If
    End If
End For
    Return Score
:End



"""


# TODO: Read File Into Word List Function

# TODO: Display Greeting Function
def show_greeting():
    print("Welcome")

# TODO: Display Instructions Function
def show_instructions():
    print("Instructions")

# TODO: Any Optional Additional Functions 

# TODO: Play Game Function

#TODO: Testing Function

#TODO: Main Program
