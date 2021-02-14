# This has nothing to do with Android
choice_str = ["ROCK" + '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
\n''', "PAPER" + '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
\n''', "SCISSORS" + '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
\n''']

# I made the yes_no module
import random, yes_no

computer_score = 0
player_score = 0
ties = 0

round_number = 1



print("\n_________________________\n\nRock, Paper, Scissors")

def player_wins():
    global player_score
    print("    You win")
    player_score += 1

def computer_wins():
    global computer_score
    print("    You lose")
    computer_score += 1


# Big function to play the game. Also allows you to import it as a mod and use this function
def play_game():
    global round_number
    global computer_score
    global player_score
    global ties

    print(f"\n* * * * * * * * * * * * *\n*        ROUND {round_number:02d}       *\n* * * * * * * * * * * * *\n")

    # User input choice 
    while True:
        player_input = input("Your turn\n1. Rock\n2. Paper\n3. Scissors\n\n")
        if player_input.lower() in ("1", "r", "rock"):
            player_choice = 0
            break
        elif player_input.lower() in ("2", "p", "paper"):
            player_choice = 1
            break
        elif player_input.lower() in ("3", "s", "scissors"):
            player_choice = 2
            break
        else:
            print("Invalid Input.\n")

    print("\n\n")

    # I made it as a list so you can weight the computer's choices by doing "choices = [[0]*3 + [1]*4, [2]*6]", etc.
    choices = [0, 1, 2]
    computer_choice = random.choice(choices)

    # Displays both moves
    print("\n    You played " + choice_str[player_choice] + "\n    The Computer played " + choice_str[computer_choice] + "\n")

    # Determines winner of round (thanks to Zvi for idea)
    if computer_choice == 0 and player_choice == 2:
        computer_wins()
    elif computer_choice == 2 and player_choice == 0:
        player_wins()

    elif computer_choice > player_choice:
        computer_wins()
    elif computer_choice < player_choice:
        player_wins()

    else:
        print("    Tie")
        ties += 1
    
    # Display score
    print(f"    Computer:{computer_score}\n    You:{player_score}\n    Ties:{ties}")
    round_number += 1

    continue_game = yes_no.yn_to_TF("\n\n\n\nContinue match? (y/n)")

    if continue_game:
        play_game()
    else:
        stop = yes_no.yn_to_TF("\nQuit game?")
        if stop:
            return
        else:
            round_number = 1
            computer_score = 0
            player_score = 0
            ties = 0
            print("\n_________________________\n")
            play_game()

play_game()
