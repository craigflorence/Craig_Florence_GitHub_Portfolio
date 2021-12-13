# In previous attempt I was trying to make a game class, and then introduce randomness and a game loop. This was too
# advanced for me just now. So this attempt is Rock Paper Scissors done much simpler.

import RPS_Class

game = RPS_Class.RpsInputGenerator()  # needed to instantiate the class, first?
game_status = True
turn_max = 3
turn_count = 1
cpu_score = 0
user_score = 0


# print(game.game_decision())
# print(game.validity_check())
print(game.comparison)
