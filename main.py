from wordtrainer import WordTrainer
from authentication import Authentication
from crossword import Crossword

# ############### Login met "Admin!" om extra woorden of talen toe te voegen of ze te verwijderen

# Asks the user to login and if they want to do a wordtrainer or crossword puzzle.
def main():
	codeUser, wordObjects = Authentication().login()
	correctAnswer = True
	while correctAnswer:
		userInput = input('Would you like to do the wordtrainer (WT) or crossword puzzle (CW): ')
		if userInput.lower() == 'wt':
			WordTrainer().keepAsking(codeUser, wordObjects)
		elif userInput.lower() == 'cw':
			correctAnswer = Crossword(wordObjects)
			
main()
