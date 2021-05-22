from database import Database 
from objectcreator import ImportData

class Users():
	def __init__(self, codeUser='', taal='', difficulty=0):
		self.name = codeUser
		self.languagePreference = taal
		self.difficulty = float(difficulty)
		
	# Creates a new user in the database.
	def createNew(self, DAL, codeUser, taal='taal', difficulty=0):
		codeUserDict = DAL.userDatabase
		codeUser = Users(codeUser, taal, difficulty)
		codeUser, wordObjects = ImportData().askLanguage(codeUser, DAL.wordDatabase)
		codeUserDict[codeUser.name] = {'name': codeUser.name, 'languagePreference': codeUser.languagePreference, 'difficulty': str(codeUser.difficulty)}
		Database.write('users.json', codeUserDict)
		return codeUser, wordObjects
		
	# Loads an existing user and asks if they want to use their previous settings.
	def loadExisting(self, DAL, codeUser):
		codeUserDict = DAL.userDatabase
		codeUser = Users(codeUserDict[codeUser]['name'], codeUserDict[codeUser]['languagePreference'], codeUserDict[codeUser]['difficulty'])
		
		if codeUser.languagePreference != 'taal':
			language = codeUser.languagePreference.split('/',1)[0]
			translateTo = codeUser.languagePreference.split('/',1)[1]
			inputList = ['yes', 'no']
			while True:
				keepSettings = input('Would you like to keep your last settings? (Yes/No) ' + codeUser.languagePreference + ' ').lower()
				if keepSettings in inputList:
					break
		else:
			keepSettings = 'no'
		if keepSettings == 'yes':
			wordObjects = ImportData().createWordsObjects(DAL.wordDatabase, language, translateTo)
		elif keepSettings == 'no': 
			codeUser, wordObjects = Users(codeUser).createNew(DAL, codeUser.name)
		return codeUser, wordObjects