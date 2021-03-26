from random import randint

# re-import our game variables
from gamePackage import variables, rules

while variables.your_choice is False:
	
	if variables.first_entry == True:
		print("_____________________________________________________________________")
		print("~~~~~~~~~~~~~~~~~*/ ROCK PAPER SCISSORS GAME */~~~~~~~~~~~~~~~~~~~~~~")
		print("_____________________________________________________________________")
		rules.accept_or_decline()
		print("_____________________________________________________________________")
		print("You want to play with me! Good luck, because you will need!")
		variables.first_entry = False


	print("I have" , variables.my_lives, "/", variables.total_lives, "lives.")
	print("You have" , variables.your_lives, "/", variables.total_lives, "lives.")
	print("______________________________________________________________________")
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

	print("Which weapon (rock, scissors, paper) do you prefer? ! Or type quit to exit\n") #\n means "new line"
	variables.your_choice = input("Choose rock, paper, or scissors: \n")

	variables.your_choice = variables.your_choice.lower()

	if variables.your_choice == "quit":
		print("You chose to quit")
		exit()

	variables.my_choice = variables.choices[randint(0, 2)]
	print("_____________________________________________________________________")

	print("Your choice is " + variables.your_choice)
	print("My choise is " + variables.my_choice)

	if variables.your_choice in variables.choices:

		if variables.my_choice == variables.your_choice:
			print("_____TIE_____")
			print("_____________________________________________________________________")
		elif variables.my_choice == "rock":
			if variables.your_choice == "scissors":
				variables.your_lives -= 1
				print("_____________________________________________________________________")
				print("_____You LOSE! player lives:", variables.your_lives)
			else:
				print("_____________________________________________________________________")
				print("_____You win! It is just coincidence! Don't be too happy!")
				variables.my_lives -= 1
		elif variables.my_choice == "paper":
			if variables.your_choice == "rock":
				variables.your_lives -= 1
				print("_____________________________________________________________________")
				print("_____You LOSE! player lives:", variables.your_lives)
			else:
				print("_____________________________________________________________________")
				print("____You win! It is just coincidence! Don't be too happy!")
				variables.my_lives -= 1
		elif variables.my_choice == "scissors":
			if variables.your_choice == "paper":
				variables.your_lives -= 1
				print("_____________________________________________________________________")
				print("____You LOSE! player lives:", variables.your_lives)
			else:
				print("_____________________________________________________________________")
				print("____You win! It is just coincidence! Don't be too happy!")
				variables.my_lives -= 1


	else:
		print("Please enter a valid choice!")

	if variables.your_lives == 0:
		rules.winorlose("lost")
	elif variables.my_lives == 0:
		rules.winorlose("won")
	else:
		variables.your_choice = False