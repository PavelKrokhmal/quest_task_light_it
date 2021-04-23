class BasePlayer:
    def __init__(self, name, HP):
        self.name = name
        self.init_HP = HP 
        self.current_HP = HP

    def reset(self):
        self.current_HP = self.init_HP

    def __str__(self):
        return "[{0}]: HP = {1}".format(self.name, self.current_HP)

    def change_HP(self, value):
        self.current_HP += value
        self.current_HP = self.current_HP if self.current_HP > 0 else 0
        self.current_HP = (
            self.current_HP if self.current_HP <= self.init_HP else self.init_HP
        )
