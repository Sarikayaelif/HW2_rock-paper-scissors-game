from gamePackage import variables

# define a win / lose function and refer to it (invoke it) in our game loop
def winorlose(status):
    if status == "won":
        pre_message = "Wow you won! You are the greatest player!"
    else:
        pre_message = "You lost! You are the loser!"

    print(pre_message + 'Would you like to play again?\n')

    choice = False

    while choice == False:
        choice = input("Y / N? ")

        if choice == "Y" or choice == "y":
            # reset the game loop and start over again
            variables.your_lives = variables.total_lives
            variables.my_lives = variables.total_lives
            variables.your_choice = False
        elif choice == "N" or choice == "n":
            # exit message and quit
            print("You chose to exit from the game. Hope to see you next time!")
            exit()
        else:
            print("Invalid entry! Please make a valid choice - Y or N\n")
            choice = False