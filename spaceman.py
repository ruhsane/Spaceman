import random

def load_word():
   f = open('spaceman_words.txt', 'r')
   words_list = f.readlines()
   f.close()

   words_list = words_list[0].split(' ')
   secret_word = random.choice(words_list)
   return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    secretWord: string, the random word the user is trying to guess.  This is selected on line 9.
    lettersGuessed: list of letters that have been guessed so far.
    returns: boolean, True only if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''



def get_guessed_word(secret_word, letters_guessed):
    '''
    secretWord: string, the random word the user is trying to guess.  This is selected on line 9.
    lettersGuessed: list of letters that have been guessed so far.
    returns: string, of letters and underscores.  For letters in the word that the user has
    guessed correctly, the string should contain the letter at the correct position.  For letters
    in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''
    # FILL IN YOUR CODE HERE...




def get_available_letters(letters_guessed):
    '''
    lettersGuessed: list of letters that have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''




def spaceman(secret_word):
    '''
    secretWord: string, the secret word to guess.
    Starts up a game of Spaceman in the command line.
    * At the start of the game, let the user know how many
      letters the secretWord contains.
    * Ask the user to guess one letter per round.
    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.
    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.
    '''
    # FILL IN YOUR CODE HERE...
    guessed_letters = []
    wrong_guessed_letters=[]

    user = user_input("Press S to start the game: ")
    if user.upper()  == "S":
        count = len(secret_word)
        tile = []
        for i in range(count):
            tile.append("_ ")
        print(" ".join(tile))

        while len(wrong_guessed_letters) != 8:
            if len(wrong_guessed_letters) == 8:
                print("Game Over! The word was: " + secret_word)
                break
            elif ("_ ") not in tile:
                print("Congrats! You Won!")
                break
            else:
                verify_letter(secret_word, tile, wrong_guessed_letters, guessed_letters)
        print("Game Over! The word was: " + secret_word)

    else:
        print("bye")




def verify_letter(secret_word, tile, wrong_guessed_letters, guessed_letters):
    letter = user_input("Guess a letter: ")
    guessed_letters.append(letter)

    if letter in secret_word:
        # print(secret_word.findall(letter))
        indexes_of_guessed = [i for i in range(len(secret_word)) if secret_word.startswith(letter, i)]
        print(indexes_of_guessed)

        for i in range(len(indexes_of_guessed)):
            tile[indexes_of_guessed[i]] = letter
        print(" ".join(tile))
        print("Guessed Letters:  " + ", ".join(guessed_letters))
        print("")
    else:
        print("The letter is not in the word!")
        print(" ".join(tile))
        print("Guessed Letters: " + ", ".join(guessed_letters))
        wrong_guessed_letters.append(letter)
        print("Wrongly Guessed Letters (You have 8 chances): " + ", ".join(wrong_guessed_letters))
        print("")



def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input

#
# secret_word = load_word()
# spaceman(load_word())
spaceman(load_word())


# do a for loop that will print josh 5 times
# for i in range(5):
#     print('josh')
#
# yeer = ['sup','suwwwooop', 'blood', 'cuz', 'fam', 'icy', 'rocks', 'bag', 'billy']
# # loop through the yeer array

# for i in range(len(yeer)):
#     print(yeer[i])

# for i in yeer:
#     print(i)


#priht 0 to 100 in loop

# for i in range(101):
#     print(i)

# for (int i = 0, i < 10, i++) {
#
# }
