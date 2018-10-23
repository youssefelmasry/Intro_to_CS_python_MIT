def playHand(hand, wordList, n):    
    score = 0
    # As long as there are still letters left in the hand:
    while calculateHandlen(hand) > 0:
    
        # Display the hand
        print(hand)
        # Ask user for input
        word = input('Enter word,, or a "." to indicate that you are finished: ')
        
        # If the input is a single period:
        if word == '.':

            # End the game (break out of the loop)
            break
            
        # Otherwise (the input is not a single period):
        else:
        
            # If the word is not valid:
            if not isValidWord(word, hand, wordList):
            
                # Reject invalid word (print a message followed by a blank line)
                print("Invalid word, please try again.\n")

            # Otherwise (the word is valid):
            else:

                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line

                current_score = getWordScore(word,n)
                score += current_score
                print("{} earned {} points. Total: {} points".format(word, current_score, score))
                
                # Update the hand 
                hand = updateHand(hand, word)

    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    if calculateHandlen(hand) == 0:
        print("Run out of letters. Total score: {}".format(score))
    else:
        print("Goodbye! Total score: {}".format(score))