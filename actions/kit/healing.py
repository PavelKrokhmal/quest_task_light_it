from ..action_own_use import ActionOwnUse

class Healing(ActionOwnUse):
    def __init__(
        self,
        name="Healing myself",
        value_range={"left": 18, "right": 25},
        is_positive=True,
    ):
        super().__init__(name, value_range, is_positive)
