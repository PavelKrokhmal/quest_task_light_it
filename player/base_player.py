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
        new_current_HP = self.current_HP + value

        if new_current_HP > self.init_HP:
            self.current_HP = self.init_HP
        elif new_current_HP < 0:
            self.current_HP = 0
        else:
            self.current_HP = new_current_HP
