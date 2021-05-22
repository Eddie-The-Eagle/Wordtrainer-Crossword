import random
from difflib import SequenceMatcher
from user import Users


class WordTrainer():
	# Keeps asking the player a new word.
	def keepAsking(self, codeUser, wordObjects):
		stopGuessing = False
		lastFourWords = ['00000', '00000', '00000', '00000']
		while not stopGuessing:
			lastFourWords = self.askTranslation(codeUser, wordObjects, lastFourWords)
		
	# Asks the player for a translation of a word.
	def askTranslation(self, codeUser, wordObjects, lastFourWords):
		word, lastFourWords = self.getRandomWord(codeUser, wordObjects, lastFourWords)
		codeUserInput = input('Input the Translation of ' + word.name + ': ')
		if codeUserInput == 'quit':
			Users(codeUser).createNew(codeUser.name, codeUser.languagePreference, codeUser.difficulty)
			quit()
		else:
			translation = word.translation
			Feedback().checkWord(codeUser, word, translation, codeUserInput)
		return lastFourWords

	# Gives the player a new random word to translate. Based on when the word was last asked and the current difficulty
	def getRandomWord(self, codeUser, wordObjects, lastFourWords):
		while True:
			number = random.randrange(0, len(wordObjects))
			chance = random.randrange(0, 100)
			word = wordObjects[number]
			if word not in lastFourWords and chance < word.chance and codeUser.difficulty >= word.difficulty:
				break
		lastFourWords.append(word)
		lastFourWords.pop(0)
		return word, lastFourWords

# Handles the feedback to the player after answering a question.
class Feedback():
	# Initial feedback loop, if the word is almost correct it gives feedback otherwise it goes to a different function.
	def checkWord(self, codeUser, word, translation, codeUserInput):
		if codeUserInput == translation:
			self.correctTranslation(codeUser, word)
		elif codeUserInput.lower() == translation.lower():
			error = 'Close, Pay attention to the capital letters.'
			self.wrongTranslation(codeUser, word, translation, error)
		elif SequenceMatcher(None, codeUserInput, translation).ratio() >= 0.75:
			error = 'Close, pay attention to the spelling'
			self.wrongTranslation(codeUser, word, translation, error)
		else:
			self.wrongTranslation(codeUser, word, translation)
			
	# Prints that the answer is correct and lowers the likelyhood of this word while increasing the overal difficulty.
	def correctTranslation(self, codeUser, word):
		print('Translation is correct\n')
		if word.chance > 10:
			word.chance -= 10
		codeUser.difficulty += 0.1
		
	# Prints that the answer is incorrect with the correct translation and increases the likelyhood of this word.
	def wrongTranslation(self, codeUser, word, translation, *args):
		print('Translation is wrong. Correct answer is ' + translation)
		if word.chance < 100:
			word.chance += 10
		for error in args:
			print(error)
			word.chance -= 5
			codeUser.difficulty += 0.05
		print('\n')
		codeUser.difficulty -= 0.05