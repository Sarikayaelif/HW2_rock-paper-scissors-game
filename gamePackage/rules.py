from gamePackage import variables

# define a win / lose function and refer to it (invoke it) in our game loop
def winorlose(status):
    if status == "won":

        pre_message = "Wow you won! I said it is just a coincidence. I think you can't dare to play again with me!"
    else:
        pre_message = "You lost! I said it will happend. You should never have played this game with me! You are the loser!"

    print(pre_message + 'Do you still dare to play athos game with me once again?\n')


    choice = False

    while choice == False:
        choice = input("Y / N? ")

        if choice == "Y" or choice == "y":
            # reset the game loop and start over again
            variables.your_lives = variables.total_lives
            variables.my_lives = variables.total_lives
            variables.your_choice = False

            variables.first_entry = True

        elif choice == "N" or choice == "n":
            # exit message and quit
            print("You chose to exit from the game. Hope to see you next time!")
            exit()
        else:
            print("Invalid entry! Please make a valid choice - Y or N\n")

            choice = False

def accept_or_decline():
    answer = ''
    while answer != 'n' and answer != 'y':
        answer = input("Do you dare to play rock-paper-scisssors game with me? Y or N \n").lower()
        if answer == 'n':
            print("You lost a chance to have an honor to play with me!")
            exit()
        elif answer != 'y':
            print("Invalid entry! Please make a valid choice - Y or N\n")
        

