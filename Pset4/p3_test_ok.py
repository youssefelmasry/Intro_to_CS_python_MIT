def isValidWord(word,hand, wordlist):
	if word in wordList:
        for i in word:
            if hand.get(i,0) < word.count(i):
                return False
        return True
    return False
    #another solution
    
    #return all([ hand.get(letter,0)>= word.count(letter) for letter in word ]) and word in wordList
