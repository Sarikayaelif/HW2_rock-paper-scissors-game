from random import randint

# re-import our game variables
from gamePackage import variables, rules

while variables.your_choice is False:
	print("_________________*/ RPS GAME */_____________________")
	print("Computer Lives:", variables.my_lives, "/", .total_lives)
	print("Player Lives:", variables.your_lives, "/", variables.total_lives)
	print("____________________________________________________")
	print("Enter your choice (rock, scissors, paper)! Or type quit to exit\n") #\n means "new line"
	variables.your_choice = input("Choose rock, paper, or scissors: \n")

	variables.your_choice = variables.your_choice.lower()

	if variables.your_choice == "quit":
		print("You chose to quit")
		exit()

	variables.my_choice = variables.choices[randint(0, 2)]

	print("user chose: " + variables.your_choice)
	print("computer chose: " + variables.my_choice)

	if variables.your_choice in variables.choices:

		if variables.my_choice == variables.your_choice:
			print("tie")
		elif variables.my_choice == "rock":
			if variables.your_choice == "scissors":
				variables.your_lives -= 1
				print("you lose! player lives:", variables.your_lives)
			else:
				print("you win!")
				variables.my_lives -= 1
		elif variables.my_choice == "paper":
			if variables.your_choice == "rock":
				variables.your_lives -= 1
				print("you lose! player lives:", variables.your_lives)
			else:
				print("you win!")
				variables.my_lives -= 1
		elif variables.my_choice == "scissors":
			if variables.your_choice == "paper":
				variables.your_lives -= 1
				print("you lose! player lives:", variables.your_lives)
			else:
				print("you win!")
				variables.my_lives -= 1


	else:
		print("Please enter a valid choice!")

	if variables.your_lives == 0:
		rules.winorlose("lost")
	elif variables.my_lives == 0:
		rules.winorlose("won")
	else:
		variables.your_choice = False