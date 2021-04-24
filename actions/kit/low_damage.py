from ..action_enemy import ActionEnemy


class LowDamage(ActionEnemy):
    def __init__(
        self,
        name="Hit enemy low damage",
        value_range={"left": 18, "right": 25},
        is_positive=False,
    ):
        super().__init__(name, value_range, is_positive)
