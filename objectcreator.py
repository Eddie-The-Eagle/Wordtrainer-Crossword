from word import Words

class ImportData():
	# Asks the user what language they want to use for translations.
	def askLanguage(self, codeUser, dataDict):
		talen, validLanguage = [], False
		for key in dataDict[next(iter(dataDict))].keys():
			talen.append(key)
		while not validLanguage:
			language = input('Enter the display language: (' + ', '.join(talen) + ') ').upper()
			if language in talen:
				validLanguage = True
		validLanguage = False
		while not validLanguage:
			translateTo = input('Enter the translation language ' + language + '? (' + ', '.join(talen) + ') ').upper()
			if translateTo in talen:
				validLanguage = True
		codeUser.languagePreference = language + '/' + translateTo
		wordObjects = ImportData().createWordsObjects(dataDict, language, translateTo)
		return codeUser, wordObjects
		
	# Creates the objects required based on the languages given by the user.
	def createWordsObjects(self, dataDict, language, translateTo):
		wordObjects = []
		for k in dataDict.keys():
			if int(k) < 7:
				wordObjects.append(Words(dataDict[k][language], dataDict[k][translateTo]))
			elif int(k) < 12:
				wordObjects.append(Words(dataDict[k][language], dataDict[k][translateTo], 1))
			else:
				wordObjects.append(Words(dataDict[k][language], dataDict[k][translateTo], 2))
		return wordObjects