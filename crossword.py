import random
from copy import copy
import re
import os
import time

class Crossword():
	def __init__(self, wordObjects):
		vertWord, horWordsList, userWordList = self.createCrossword(wordObjects)
		self.vertWord = vertWord
		self.horWordCounter = len(horWordsList)
		self.horWordsList = horWordsList
		self.userHorWordList = userWordList
		
		self.printCrossword()
		self.enterWord()
			
	# Generates a crossword puzzle.
	def createCrossword(self, wordObjects):
		crossWordComplete = False
		while not crossWordComplete:
			horWord = self.getRandomWord(wordObjects)
			newWordObjects = copy(wordObjects)
			newWordObjects.remove(horWord)
			vertWordsList, userWordList = [], []
			for char in horWord.translation:
				for _ in range(0, len(newWordObjects)):
					word = self.getRandomWord(newWordObjects)
					for pos, letter in enumerate(word.translation):
						foundLetter = False
						if letter == char:
							vertWordsList.append([word, pos])
							userWordList.append(word.translation)
							newWordObjects.remove(word)
							foundLetter = True
							break
					if foundLetter == True:
						break
				if foundLetter == False:
					break
			if foundLetter == True:
				crossWordComplete = True
		for index, word in enumerate(userWordList):
			userWordList[index] = re.sub('[a-z]','_',word)
		return horWord, vertWordsList, userWordList
		
	# Gets a random word from the word list.
	def getRandomWord(self, wordObjects):
		number = random.randrange(0, len(wordObjects))
		word = wordObjects[number]
		return word
		
	# Handles userinput and checks the answers.
	def enterWord(self):
		solvedPuzzle, correctInput = False, False
		while not correctInput:
			try:
				pos = int(input('\nEnter the position of the word: '))
				if pos > len(self.userHorWordList)+2:
					print(pos, "isn't a valid position!")
				else:
					correctInput = True
			except:
					print("That's not a valid option!")
		if pos < len(self.userHorWordList)+1:
			horWord = input('Enter the translation of ' + str(self.horWordsList[pos-1][0].name) + ': ')
			if horWord == self.horWordsList[pos-1][0].translation:
				self.userHorWordList[pos-1] = horWord
				print(horWord, 'is the correct translation of', self.horWordsList[pos-1][0].name)
			else:
				print(horWord, 'is not the correct translation of', self.horWordsList[pos-1][0].name)
		elif pos < len(self.userHorWordList)+2:
			userVertWord = input('Enter the Horizontal Word: ')
			if userVertWord == self.vertWord.translation:
				solvedPuzzle = True
				print('You\'ve succesfully solved the crossword puzzle!!!')
		if solvedPuzzle == False:
			time.sleep(2)
			self.printCrossword()
			self.enterWord()

	# prints the crossword puzzle on the screen.
	def printCrossword(self):
		yellow = '\033[1;33;40m'
		white = '\033[1;37;40m'
		print(white)
		os.system('cls')
		printList = []
		for i in range(len(self.userHorWordList)):
			printList.append('{:<{}s}'.format(str(i+1) + '. ' + self.horWordsList[i][0].name, 20) + '{:>{}s}'.format(" ".join(self.userHorWordList[i]) + ' ', 40 + len(self.horWordsList[i][0].translation) * 2 - self.horWordsList[i][1] * 2 - 20))
		for line in range(len(printList)):
			printList[line] = str(printList[line][0:40] + yellow + '[' + printList[line][40:41] + ']' + white + printList[line][41:])
			print(printList[line])
		print('\n' + yellow + str(len(printList)+1) + '. Vertical word = ' + str(re.sub('[a-z]','_ ',self.vertWord.name)) + white)
