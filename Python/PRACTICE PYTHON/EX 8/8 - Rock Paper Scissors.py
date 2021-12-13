# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out
# a message of congratulations to the winner, and ask if the players want to start a new game)

# FAILURE

import random

rps_dict = {
    1: "Rock",
    2: "Paper",
    3: "Scissors"
}


class RockPaperScissors:
    def __init__(self, number_of_turns, rules):
        self.number_of_turns = number_of_turns
        self.rules = rules

    def computer_player(self):
        random_int = random.randint(1, len(rps_dict))
        cpu_choice = f"I choose {self.rules[random_int]}"
        return cpu_choice

    def comparison(self, player_choice, cpu_choice):
        if player_choice == cpu_choice:
            return "It's a tie!"
        elif player_choice == 'rock':
            if cpu_choice == 'scissors':
                return "Rock wins!"
            else:
                return "Paper wins!"
        elif player_choice == 'scissors':
            if cpu_choice == 'paper':
                return "Scissors win!"
            else:
                return "Rock wins!"
        elif player_choice == 'paper':
            if cpu_choice == 'rock':
                return "Paper wins!"
            else:
                return "Scissors win!"
        else:
            return "Invalid input! You have not entered rock, paper or scissors, try again."

    def main_loop(self):
        turn = 0
        self.number_of_turns = int(input("Out of how many?\n Turns: "))
        while turn != self.number_of_turns:
            player_choice = input("Choose ROCK, PAPER or SCISSORS").upper()
            cpu_choice = self.computer_player()
            turn += 1
    main_loop()

RockPaperScissors()