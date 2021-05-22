from database import Database 

class AdminPanel():
	# Gives the admin a option on where to go next and sends him there.
	def chooseAction(self):
		dataDict = Database.read('words.json')
		while True:
			action = input('Choose an action: \n1. Add Word.\n2. Add Language\n3. Remove Word.\n4. Remove Language\n5. Logout \n').lower()
			if action in ('1,2,3,4,5'):
				if action == '1':
					dataDict = self.addWord(dataDict)
				elif action == '2':
					dataDict = self.addLanguage(dataDict)
				elif action == '3':
					dataDict = self.removeWord(dataDict)
				elif action == '4':
					dataDict = self.removeLanguage(dataDict)
				elif action == '5':
					break
				Database.write('words.json', dataDict)
			else:
				print('Incorrect input')
	
	# Adds a new word to the database and asks for a translation for the word in all existing languages.
	def addWord(self, dataDict):
		dataDictCount = str(int(max(dataDict, key=int))+1)
		for language in dataDict[next(iter(dataDict))].keys():
			vertaling = input('Vul het ' + language +  ' woord in: ')
			if dataDictCount in dataDict.keys():
				dataDict[dataDictCount][language] = vertaling
			else:
				dataDict[dataDictCount] = {}
				dataDict[dataDictCount][language] = vertaling
		return dataDict
	
	# Adds a language to the database and asks to enter translation for all existing words.
	def addLanguage(self, dataDict):
		language = input('Enter the abbreviation of the language you would like to add: ')
		languageToSee = input('Enter the abbreviation of the language you would like to see when adding translations: ')
		for key in dataDict.keys():
			vertaling = input('Vul het ' + language +  ' woord in van "' + dataDict[key][languageToSee] + '": ')
			dataDict[key][language] = vertaling
		return dataDict
		
	# Removes a word from the database.
	def removeWord(self, dataDict):
		removedWord = True
		while removedWord:
			word = input('Enter the word you would like to remove: ')
			for key in dataDict.keys():
				for dictWord in dataDict[key].values():
					if word == dictWord:
						print('Removed the words: ' + str(dataDict[key]))
						del dataDict[key]
						return dataDict
			removedWord = False
		else:
			print('Couldn\'t remove the word: ' + word)		
			return dataDict
		
	# Removes a language from the database.
	def removeLanguage(self, dataDict):
		language = input('Enter the abbreviation of the language you would like to remove: ')
		try:
			for key in dataDict.keys():
				del dataDict[key][language]
		except KeyError:
			print('Couldn\'t remove', language, 'language')
		return dataDict
