
import random

# function to get the player's choice

def get_player_choice():

    choice = input("Enter rock, paper, or scissors: ").lower()

    while choice not in ["rock", "paper", "scissors"]:

        print("Sorry, that is not a valid choice. Please try again.")

        choice = input("Enter rock, paper, or scissors: ").lower()

    return choice

# function to determine the winner

def determine_winner(player, computer):

    if player == computer:
        return "tie"

    elif player == "rock" and computer == "scissors":
        return "win"

    elif player == "paper" and computer == "rock":
        return "win" 

    elif player == "scissors" and computer == "paper":
        return "win"

    else:
        return "loss"

# beginning of the game 

print("Welcome to Rock Paper Scissors!")

rounds = int(input("How many rounds would you like to play? "))

while rounds % 2 == 0:

    print("Sorry, the number must be an odd number.")

    rounds = int(input("How many rounds would you like to play? "))

player_wins = 0

computer_wins = 0

rounds_played = 0 

# play the rounds and determine each winner

while rounds_played < rounds: 

    player = get_player_choice()

    computer = random.choice(["rock", "paper", "scissors"])

    print ("The computer chose", computer)

    result = determine_winner(player, computer)

    if result == "tie": 

        print("Tie! Play again.")

    elif result == "win":
        print("You won!")

        player_wins += 1

        rounds_played += 1
        

    else:
        print("You lost!")

        computer_wins += 1

        rounds_played += 1

# print results 

print("-------------------------------------------")

print("Score - You: ", player_wins, "Computer: ", computer_wins)

if player_wins > computer_wins: 
    print("You win!!!")

else:
    print("Computer wins!!!")

print("Thanks for Playing!")



    














    


    































