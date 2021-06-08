import random

rps = ["Rock", "Paper", "Scissors"]

computer = random.choice(rps)
player_count = 0
computer_count = 0

while True:
    player = input("Rock, Paper, Scissors: ")
    computer = random.choice(rps)
    if player == computer:
        print("Tie!")
    elif player == "Rock" or player == "rock" or player == "R" or player == "r":
        if computer == "Paper":
            print("Player choose", player, "Computer choose", computer, "\nYou lose!")
            computer_count = computer_count + 1
        else:
            print("Player choose", player, "Computer choose", computer, "\nYou win!")
            player_count = player_count + 1
    elif player == "Paper" or player == "paper" or player == "P" or player == "p":
        if computer == "Scissors":
            print("Player choose", player, "Computer choose", computer, "\nYou lose!")
            computer_count = computer_count + 1
        else:
            print("Player choose", player, "Computer choose", computer, "\nYou win!")
            player_count = player_count + 1
    elif player == "Scissors" or player == "scissors" or player == "S" or player == "s":
        if computer == "Rock":
            print("Player choose", player, "Computer choose", computer, "\nYou lose!")
            computer_count = computer_count + 1
        else:
            print("Player choose", player, "Computer choose", computer, "\nYou win!")
            player_count = player_count + 1
    else:
        print("Invalid input!")

    print("\nPlayer Score: ", player_count, "\nComputer Score: ", computer_count)

    playAgain = input("\nPlay again? Enter 'y' for yes or 'n' for no. ")
    if playAgain in ["Yes", "yes", "Y", "y"]:
        pass
    elif playAgain in ["No", "no", "N", "n"]:
        print("\nThank you for playing :)")
        break
    else:
        break