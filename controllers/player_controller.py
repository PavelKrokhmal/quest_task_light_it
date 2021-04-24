from .base_controller import BaseController
from utils import wait_for_correct_key

from actions import ActionOwnUse

class PlayerController(BaseController):
    def __init__(self, player, actions):
        super().__init__(player, actions)

    def get_actions(self):
        return "\n".join(
            list(
                map(
                    lambda item: " [{0}] {1}".format(item[0], item[1]),
                    self.actions.items(),
                )
            )
        )

    def get_string_actions_keys(self):
        return list(map(str, self.actions.keys()))

    def get_selected_action(self):
        print(" Available actions:")
        print(self.get_actions())
        
        return self.actions[int(wait_for_correct_key(" Your action: ", self.get_string_actions_keys()))]


