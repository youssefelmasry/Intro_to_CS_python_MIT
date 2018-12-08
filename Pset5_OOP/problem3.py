class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        super().__init__(text)
        

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        best_shift = 0
        real_words = 0
        best_decrypted_message = ''
        for s in range(26):
            list_message = self.apply_shift(s)
            num_valid_words = 0
            for j in list_message.split(' '):
                if is_word(self.valid_words, j):
                    num_valid_words += 1
            if num_valid_words > real_words:
                real_words = num_valid_words
                best_shift = s
                best_decrypted_message = list_message

        return(best_shift, best_decrypted_message)
                