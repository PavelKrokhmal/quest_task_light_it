from .action_base import ActionBase

class ActionEnemy(ActionBase):
    def __init__(self, name, value_range, is_positive):
        super().__init__(name, value_range, is_positive)
