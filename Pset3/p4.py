def isInword(secretWord, letter_guess):
    return letter_guess in secretWord

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''

    print("Welcome to the game, Hangman!\nI am thinking of a word that is %d letters long" %len(secretWord))
    print('----------')
    gues_left = 8
    gues_letter = ''
    letters_guessed = []
    while gues_left>0:
        if not isWordGuessed(secretWord, letters_guessed):
            print("you have %d gusses left." %gues_left)
            print("Available letters: %s" %getAvailableLetters(letters_guessed))
            gues_letter = input("Please guess a letter: ")
            if gues_letter in letters_guessed:
                print("Oops! You've already guessed that letter: %s" %getGuessedWord(secretWord, letters_guessed))
                print('----------')
            else:
                letters_guessed.append(gues_letter)
                if isInword(secretWord, gues_letter):
                    print("Good guess: %s" %getGuessedWord(secretWord,letters_guessed))
                    print('----------')
                else:
                    print("Oops! That letter is not in my word: %s" %getGuessedWord(secretWord,letters_guessed))
                    print('----------')
                    gues_left -= 1
        else:
            print("Congratulations, you won!")
            break
    else:
        print("Sorry, you ran out of guesses. The word was %s. " %secretWord)