# DAL Bestandsnaam: Data access layer

import json
import io
import os

folderPath = os.path.dirname(os.path.realpath(__file__)) + '\\' 

class Database():
	def __init__(self):
		self.userDatabase = self.read('users.json')
		self.wordDatabase = self.read('words.json')
	
	# Handles reading of the files.
	@staticmethod
	def read(fileName):
		try:
			with io.open(folderPath + fileName, 'r', encoding='utf8') as file:
				dataReadable = file.read()
				dataDict = json.loads(dataReadable)
				file.close()
		except FileNotFoundError:
			dataDict = {}
			Database.write(fileName, dataDict)
		return dataDict
	
	# Handles writing to the files.
	@staticmethod
	def write(fileName, data):
		try:
			to_unicode = unicode
		except NameError:
			to_unicode = str
		data = json.dumps(data, indent=4, sort_keys=True, separators=(',', ': '), ensure_ascii=False)
		with io.open(folderPath + fileName, 'w+', encoding='utf8') as file:
			file.write(to_unicode(data))
			file.close

if __name__ == "__main__":
	dal = Database()
	userDatabase = dal.userDatabase
	userDatabase['Jan'] = 'Jan'
	print(userDatabase)	