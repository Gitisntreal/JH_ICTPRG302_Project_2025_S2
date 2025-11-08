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
    """ This function is used to detect the letters within guess word (inputted by player).
    At base it will give a score 0 to all the letters then set the score of 2 if the letter is in the correct position of the target word.
    If the score is still set at 0 and the guess letter is within the target word then it will set a score 1.
        Arguments
        ---------
        guess : str
        the word that is guessed by the player
        target : str
        targeted word that needs to be guessed
        Returns:
        -------
        list
        2 = exact match of target word ( correct letter and position)
        1 = matched letter within the target word but misplaced (correct letter)
        0 = no match (letter is not in target word)
        
        Examples
        --------
        guess_word = 'hello'
        target_word = 'train'
        score = score_guess(guess_word, target_word)
        print('Score:', score, 'Expected:', [0, 0, 0, 0, 0])
        #output
        [0, 0, 0, 0, 0][0, 0, 0, 0, 0]
        guess_word = 'world'
        target_word = 'hello'
        score = score_guess(guess_word, target_word)
        print('Score:', score, 'Expected:', [0, 0, 0, 0, 0])
        #output
        [0, 1, 0, 2, 0][2, 2, 2, 2, 2]
        """
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
def read_words_into_list(filename):
    """ Reads the target words file and store them in a list.
  Arguments
    ---------
    filename : str
    the name/path of text file in which contains word to be read.
    
    Returns:
    -------
    list
        a list that contains all words in read mode from t he file.
        
    Examples
    --------
    # word_list read_words_into_list('target_words.txt)
    # print(word_list)
    [aback, abase, abate, abbey, abbot]
    """
    word_list = []
    with open(filename, 'r') as file:
        for line in file:
            word = line.strip()
            word_list.append(word)
    return word_list

# Test Case 4
## Arrange
all_word_filename = "all_words.txt"
## Act
all_word_list = read_words_into_list(all_word_filename)
## Assert
print("Got:", all_word_list[:5], "Expected:", ['aahed', 'aalii', 'aargh', 'aarti', 'abaca'])

# Test Case 5
## Arrange
target_word_filename = "target_words.txt"
## Act
target_word_list = read_words_into_list(target_word_filename)
## Assert
#TODO: Create the statement to show the last 5 words and check that they are correct
## Assert
print("Got:", target_word_list[:5], "Expected:", ['aback', 'abase', 'abate', 'abbey', 'abbot'])

#Creating a random word fucntion
import random
def random_target_word(random_word_list):
    """ 
    select a random word within the targeted word list variable and return it.
  Arguments
    ---------
    word_;ist : list
        A list of containing all the targetted word taht they player must guess.
    
    Returns:
    -------
    str
        a randomly selected word from the target words list.

        
    Examples
    --------
    # target_words = ['aback', 'abase', 'abate', 'abbey', 'abbot']
    # random_word(words)
    output: 'abase'
    """
    # TODO: Count the words in the word list
    word_count = len(random_word_list)
    # TODO: Select a random number between 0 and the number of words in the list
    random_list = random.randint(0, word_count - 1)
    # TODO: Return the word at the random number's position
    return random_word_list[random_list]

# Test Case 6
# TODO: Set list of words to ["apple", "banana", "cherry"]
words = ['apple', 'banana', 'cherry']
for word_count in range(5):
    # TODO: Call random word with the list of words
    targetted_word = random_target_word(words)
    # TODO: Display the randomly selected word
    print('Random targetted words:', targetted_word)
 
    
    
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
