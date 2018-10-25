def playGame(wordList):    
    first = True
    while True:
        action = input("Enter n to deal a new hand, r to replay the last hand, or e to end the game: ")
        if action == 'n' or action == 'r':
            if action == 'r' and first:
                print("You have not played a hand yet. Please play a new hand first!")
                continue
            while True:
                who = input("\nEnter u to have yourself play, c to have the computer play: ")
                if who == 'u' or who == 'c':
                    break
                else:
                    print("Invalid command!")
                    continue
            if action == 'n':
                first = False
                current_hand = dealHand(HAND_SIZE)
                if who == 'u':
                    playHand(current_hand, wordList, HAND_SIZE)
                else:
                    compPlayHand(current_hand, wordList, HAND_SIZE)
            elif action == 'r':
                if who == 'u':
                    playHand(current_hand, wordList, HAND_SIZE)
                else:
                    compPlayHand(current_hand, wordList, HAND_SIZE)
        elif action == 'e':
            break
        else:
            print("Invalid command.")