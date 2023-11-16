# Preethi Ann Jacob
# 16 Nov 2023

# Python program to demonstrate Hangman Game Logic

# -------------------------Preliminaries------------------
# 1.	The collection Module in Python provides different types of containers. A Container is an object that is used to store different objects and provide a way to access the contained objects and iterate over them. Some of the built-in containers are Tuple, List, Dictionary, etc. # A counter is a sub-class of the dictionary. It is used to keep the count of the elements in an iterable in the form of an unordered dictionary where the key represents the element in the iterable and value represents the count of that element in the iterable.
# 		e.g Counter(['B','B','A','B','C','A','B', 'B','A','C']) gives Counter({'B': 5, 'A': 3, 'C': 2})
# 2. 	The random.choice() method returns a randomly selected element from the specified sequence.
# 		The sequence can be a string, a range, a list, a tuple or any other kind of sequence.
# 3.	"pip install random-word" to use the module random_word
# 4.	string.count(value, start, end): count() method returns the number of times a specified value appears in the string.

# ---------------------------------------------------------

# ----------------------Code to select a random word from given string----------
# import random
# someWords = '''apple banana mango strawberry orange grape pineapple apricot lemon coconut watermelon cherry papaya berry peach lychee muskmelon'''
# someWords = someWords.split(' ') # split the string to list
# word=random.choice(words) # randomly select an element from the specified list
#----------------------------------------------------------------------------

from collections import Counter
from random_word import RandomWords

while(True):
	try:
		print("Starting the HANGMAN game. Ready for it?? \n If not ready, press Ctrl+C anytime\n")
			
		# Code to select a random word 
		r = RandomWords()
		word = r.get_random_word() # Return a single random word

		print("Guess the word!")
			
		# Print empty spaces for filling up the letters of the word e.g. _ _ _ _ for duck
		for i in word:
			print('_',end=' ')
		print()

		lettersSoFarGuessed = ''
		chances = len(word)+2 # No of chances = no of letters in the word + 2 extra chances
		# Game stops when there are no more chances OR when player Wins
		while (chances!=0):
			guess = str(input("\n(No of chances left: "+str(chances)+") Enter a letter to guess: "))
			chances-=1
			if not guess.isalpha():
				print("Enter only alphabets")
				continue
			elif len(guess)>1:
				print("Enter only a single letter")
				continue
			elif guess in lettersSoFarGuessed:
				print("You have already guessed that letter")
				continue

			# If letter is guessed correctly
			if guess in word:
				# k stores the number of times the guessed letter occurs in the word
				k = word.count(guess)
				for _ in range(k):
					lettersSoFarGuessed +=guess # The guess letter is added as many times as it occurs

			# Print the word
			for char in word:
				# If user has guessed all the letters => Once the correct word is guessed fully, The game ends even if chances remains
				if (Counter(lettersSoFarGuessed) == Counter(word)):
					print("The word is: ", word)
					print('Congratulations, You won!')
					exit()
				elif ( char in lettersSoFarGuessed ):
					print(char, end = ' ')
				else:
					print('_', end =' ')

		# If user has used all of his chances
		if chances==0:
			print('\nYou lost! Try again..')
			print('The word was {}\n\n'.format(word))
	except KeyboardInterrupt: # KeyboardInterrupt means Ctrl+C is clicked
		print('\nBye! Try again')
		exit()

