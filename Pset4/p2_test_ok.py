def updateHand(hand, word):
	#make a copy of the dictionary to not change in the original one
	h = hand.copy()
	for i in word:
		h[i] -=1
	return h