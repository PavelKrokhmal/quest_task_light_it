class BaseController:
    def __init__(self, player, actions):
        self.player = player
        self.actions = {}

        for index, action in enumerate(actions):
            self.actions[index + 1] = action

    def get_selected_action(self):
        raise NotImplementedError

    def apply_action(self, action):
        raise NotImplementedError
