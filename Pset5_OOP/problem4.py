def decrypt_story():
	dec_story = CiphertextMessage(get_story_string())
	return dec_story.decrypt_message()