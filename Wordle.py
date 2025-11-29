# Assessment Task 3 (AT3): Project
#
# Author: Jason Huynh
# Student ID: 20134959
#
# Course: ICT40120 (Data Science and AI)
# Lecturer: Chris

# TODO: Add Import statements (if needed)
DEBUG = False
# Variables and Constants
# TODO: Define Constants
# definition: it is a value in which does not change, where they stay the same throughout the program

# TODO: Define Variables 
# definition: it is a named container/ placeholder that holds data into the named container in which the program use to recall to process the stored data.

# Application Functions
# TODO: Score Guess Function
# Jason Huynh 20134959 - 5/11/2025
def score_guess(guess: str, target: str) -> list[int]:
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
    for i, (g_char, t_char) in enumerate (zip(guess, target)):
        if g_char == t_char:
            score[i] = 2
            target_letter[i] = None
    for i, g_char in enumerate(guess):
        if score[i] == 0 and g_char in target_letter:
            score[i] = 1
            target_letter[target_letter.index(g_char)] = None
    return score
# ok what this new code does is the same thing as the previous code but instead it has been improved where it is less index heavy 

# Human friendly score display
def display_score(score, word_guess):
    """ 
    Display a human friendly score of the guesses using the score list.
   Arguments
    ---------
    score : list 
        a list of integers that represts the result of each letter in the guessed word.
    word_guess : str
        words guessed by the player.
    
    Returns:
    -------
    None
        A function in which prints the score and guess word to the console.
   
    Examples
    --------
    # display_score([2, 0, 1, 1, 2], 'aback')
    # X-??X
    # A B A C K
    """
    symbols = {0:' - ', 1:' ? ', 2:' X '}

    score_output = ''.join(symbols[value] for value in score)
    word_output = ''.join(word_guess)
    
    """
    for count in range(len(score)):
         if score[count] == 0:
             score_output += ' - '
         elif score[count] == 1:
             score_output += ' ? '  
         elif score[count] == 2:
             score_output += ' x '

    # TODO: For count in range 1 to length of score:
    for count in range(len(score)):
        word_output += word_guess[count]
        word_output += ' '
    # I dont think this is needed anymore but for assignment purpose I will leave it be.
    """
    print(score_output)
    print(word_output)

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
        a list that contains all words in read mode from the file.
        
    Examples
    --------
    # word_list read_words_into_list('target_words.txt')
    # print(word_list)
    [aback, abase, abate, abbey, abbot]
    """
    word_list = []
    with open(filename, 'r') as file:
        for line in file:
            word = line.strip()
            word_list.append(word)
    return word_list

#Creating a random word fucntion
import random
from typing import Sequence
def random_target_word(words: Sequence[str]) -> str:
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
    """
    # TODO: Count the words in the word list
    word_count = len(random_word_list)
    # TODO: Select a random number between 0 and the number of words in the list
    random_list = random.randint(0, word_count - 1)
    # TODO: Return the word at the random number's position
    return random_word_list[random_list]
    # Again I don't think i need this anymore but leaving it for the assignment.
    """
    return random.choice(words)


# TODO: Display Greeting Function
def show_greeting():
    print("Welcome To the Game")
    print('Play Game?')
    start = input('Enter any key to play the game or "Q" to quit:')
    if start in ['q', 'Q']:
        print('Goodbye!')
        sys.exit()
    return

# TODO: Display Instructions Function
def show_instructions():
    display_instruction = input('Would you like to see the instructions? (yes/no): ')
    if display_instruction in ['yes', 'y', 'ye', 'yea', 'ya']:
        print('\n How to Play The Game')
        print('\n1. You have a limited amount of guesses to find the targeted word.')
        print('\n2. Each guess must be a valid word of the 5 lettered words')
        print('\n3. After each guess, you will see a display score/clure:')
        print('\n   X = Correct letter in correct position.')
        print('\n   ? = Correct letter in wrong position.')
        print('\n   - = incorrect letter')
    else:
        print('\nSkipping instructions.\n ')
    print('Game Starting')
    return

# TODO: Any Optional Additional Functions 
def amount_of_guesses() -> int:
    while True:
        try:
            max_guesses = int(input('How many guesses do you want (1-10)?'))
            if 1 <= max_guesses <=10:
                return max_guesses
            print('Please enter a number that is between 1 and 10.')
        except ValueError:
            print('Please enter in a number only!')


def valid_guesses(all_words: list[str]) -> str:
    while True:
        guess = input('What is your guess?: ').strip().lower()
        if len(guess) != 5:
            print('Invalid guess: Word must be 5 letters long!')
            continue
        if guess not in all_words:
            print('Invalid guess: This word is not in the word list.')
            continue
        return guess


# TODO: Play Game Function
import sys
def play_game() -> None:


        
    else:
        show_greeting()
    username = input('Enter your username: ')
    print('Hello, ', username.title()  )
    show_instructions()

    
    while True:
        max_guesses = 6
        target_word_list = 'target_words.txt'
        target_words = read_words_into_list(target_word_list)
        all_words_list = 'all_words.txt'
        all_words = read_words_into_list(all_words_list)
        target_words = random_target_word(target_words)
        for attempt in range(1, max_guesses + 1):
            while True:
                guess = input(f'Attempt {attempt}/{max_guesses}:').lower()
                if len(guess) != 5:
                    print('Invalid guess. Word must be 5 letters long.')
                    continue
                if guess not in all_words:
                    print('Invalid guess: This word is invalid')
                    continue
                break
            if guess == target_words:
                print(f'Congratulation, {username.title()} have guessed the correct word.')
                break

            score = score_guess(guess, target_words)
            display_score(score, guess)
        else:
            print(f'Game over! {username.title()}... should of guessed the word {target_words}.')
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again not in ['yes', 'y']:
            print(f"\nGoodbye {username.title()}!")
            break
        print("\nStarting a new game...\n")

        
   
    
    
        

#TODO: Testing Function (Test Game)
def test_game():
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
    target_word_list_test = read_words_into_list(target_word_filename)
    ## Assert
    # TODO: Create the statement to show the last 5 words and check that they are correct
    ## Assert
    print("Got:", target_word_list_test[:5], "Expected:", ['aback', 'abase', 'abate', 'abbey', 'abbot'])

    # Test Case 6
    # TODO: Set list of words to ["apple", "banana", "cherry"]
    testingrandom_words = ['apple', 'banana', 'cherry']
    for word_count in range(5):
    # TODO: Call random word with the list of words
        testing_target_word = random_target_word(testingrandom_words)
    # TODO: Display the randomly selected word
        print('Random targetted words:', testing_target_word)

#TODO: Main Program
if DEBUG:
    test_game()
else: 
    play_game()