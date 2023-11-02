#-----------------------------------------------------------------------------------------
"""# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

# write hello world
"""

import random

elements = ["rock", "paper", "scissors"]
beats = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

def play_game():
    
    is_terminated=False
    wins = 0
    rounds = 0
    
    while not is_terminated:
        # Get the player's choice
        rounds += 1

        player_choice = input("Choose rock, paper, or scissors: ").lower()

        # Validate the player's choice
        if player_choice not in elements:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        # Generate the computer's choice
        computer_choice = random.choice(elements)

        # Check for a win, loss, or tie
        if player_choice == computer_choice:
            print(f"It's a tie! Both players chose {player_choice}.")
            
        elif beats[player_choice] == computer_choice:
            print(f"Congratulations! You won with {player_choice} against {computer_choice}.")
            wins += 1
        else:
            print(f"Sorry, you lost. {computer_choice} beats {player_choice}.")

        # Check if the player wants to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print(f"Your score is {wins} of {rounds} rounds")
            break

play_game()