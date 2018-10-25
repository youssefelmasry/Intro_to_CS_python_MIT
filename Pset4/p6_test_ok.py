def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.

      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1    
    """
    first = True
    while True:
    	action = input("Enter n to deal a new hand, r to replay the last hand, or e to end the game: ")
    	if action == 'r' and first:
    		print("You have not played a hand yet. Please play a new hand first!")
    	elif action == 'n':
    		current_hand = dealHand(HAND_SIZE)
    		playHand(current_hand, wordList, HAND_SIZE)
    		first = False
    	elif action == 'r':
    		playHand(current_hand, wordList, HAND_SIZE)
    	elif action == 'e':
    		break
    	else:
    		print("Invalid command.")
