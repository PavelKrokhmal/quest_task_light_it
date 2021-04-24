import random

# Balancer предназначен для того чтобы решить проблему
# слишком частого появления одного и того же игрока подряд.
class Balancer:
    def __init__(
        self, player1_controller, player2_controller, max_same_battle_pairs_counter=2
    ):
        self.player1_controller = player1_controller
        self.player2_controller = player2_controller
        self.max_same_battle_pairs_counter = max_same_battle_pairs_counter
        self.current_counter = 0
        self.last_battle_pairs = []

    def reset(self):
        self.current_counter = 0
        self.last_battle_pairs = []

    def update_last_pairs(self, pairs, current_counter):
        self.last_battle_pairs = pairs
        self.current_counter = current_counter

    def get_battle_pair(self):

        pairs = random.sample([self.player1_controller, self.player2_controller], 2)

        if self.last_battle_pairs == pairs:
            if self.current_counter == self.max_same_battle_pairs_counter:
                self.update_last_pairs(pairs[::-1], 1)
            else:
                self.update_last_pairs(pairs, self.current_counter + 1)
        else:
            self.update_last_pairs(pairs, 1)

        return self.last_battle_pairs
