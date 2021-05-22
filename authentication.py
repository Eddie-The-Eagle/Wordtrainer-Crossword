from user import Users
from database import Database
from admin import AdminPanel


class Authentication():
	# Asks for the username
	def login(self):
		DAL = Database()
		user = input('Enter your name: ')
		user, wordObjects = self.initializeUser(user, DAL)
		return user, wordObjects
		
	#Checks if the user is an admin, new user or existing user
	def initializeUser(self, user, DAL):
		if user == 'Admin!':
			AdminPanel().chooseAction()
		if user in DAL.userDatabase:
			user, wordObjects = Users().loadExisting(DAL, user)
		else:
			user, wordObjects = Users(user).createNew(DAL, user)
		return user, wordObjects