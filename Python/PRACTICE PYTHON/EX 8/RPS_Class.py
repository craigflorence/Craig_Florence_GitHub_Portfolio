from random import choice


class RpsInputGenerator:
    rps = ["ROCK", "PAPER", "SCISSORS"]
    win_lose_dict = {"ROCK": 1, "PAPER": 2, "SCISSORS": 3}

    @staticmethod
    def game_decision(self):  # Gives Rock paper or scissors
        random_choice = choice(RpsInputGenerator.rps)
        return random_choice

    @staticmethod
    def validity_check(self):  # Makes sure user types in Rock paper or scissors and returns it.
        while True:
            v_player_choice = input("Rock, Paper or Scissors?\n >>>: ")
            player_choice_upper = v_player_choice.upper()
            if player_choice_upper in RpsInputGenerator.rps:
                break
            else:
                print("Invalid choice. Try again!")
        return player_choice_upper

    @staticmethod
    def comparison(self):  # Compares CPU to User and decides the winner.
        cpu_val_to_dict = RpsInputGenerator.win_lose_dict.get(RpsInputGenerator.validity_check())
        print(cpu_val_to_dict)
