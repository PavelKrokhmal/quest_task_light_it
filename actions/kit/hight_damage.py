from ..action_enemy import ActionEnemy


class HightDamage(ActionEnemy):
    def __init__(
        self,
        name="Hit enemy hight damage",
        value_range={"left": 10, "right": 35},
        is_positive=False,
    ):
        super().__init__(name, value_range, is_positive)
