from .base_player import BasePlayer


class Player(BasePlayer):
    def __init__(self, name, HP=100):
        super().__init__(name, HP)

    def is_alive(self):
        return self.current_HP != 0
