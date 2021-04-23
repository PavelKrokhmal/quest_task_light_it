import random
from typing import Any, List

from .base_controller import BaseController

from actions import ActionEnemy, ActionOwnUse

class BotController(BaseController):

    CONST_LOW_HP_PERCENT = 35
    CONST_NORMAL_HP_PERCENT = 75
    CONST_MAX_RANDOM_MULTIPLIER = 5

    def __init__(self, player, actions):
        super().__init__(player, actions)

        self.actions_for_own_use = self.get_actions_for_own_use()
        self.actions_for_enemy = self.get_actions_for_enemy()

    def get_actions_for_own_use(self):

        return list(
            filter(
                lambda action: isinstance(action, ActionOwnUse),
                self.actions.values(),
            )
        )

    def get_actions_for_enemy(self):
        return list(
            filter(
                lambda action: isinstance(action, ActionEnemy), self.actions.values()
            )
        )

    def get_random_multiplier(self):
        return random.randint(1, self.CONST_MAX_RANDOM_MULTIPLIER)

    def get_random_action_from_list(self, actions):
        return random.choice(actions)

    def get_random_mixed_actions_list(self, actions):
        return random.sample(actions, len(actions))

    def get_random_action_due_low_HP(self):
        return self.get_random_action_from_list(
            self.get_random_mixed_actions_list(
                self.actions_for_own_use * self.get_random_multiplier()
                + self.actions_for_enemy
            )
        )

    def get_selected_action(self):
        bot_selected_action = None
        if self.is_low_HP():
            bot_selected_action = self.get_random_action_due_low_HP()
        elif self.is_normal_HP():
            bot_selected_action = self.get_random_action_from_list(
                self.actions_for_enemy
            )
        else:
            bot_selected_action = self.get_random_action_from_list(
                [*self.actions.values()]
            )

        print(" Bot selected: {0}".format(bot_selected_action))

        return bot_selected_action

    def is_low_HP(self):
        return (
            self.player.current_HP
            <= self.player.init_HP * self.CONST_LOW_HP_PERCENT / 100
        )

    def is_normal_HP(self):
        return (
            self.player.current_HP
            >= self.player.init_HP * self.CONST_NORMAL_HP_PERCENT / 100
        )

    def apply_action(self, action):
        action_value = action.get_random_value()
        print("{0} points HP for {1}".format(action_value, "myself" if isinstance(action, ActionOwnUse) else "enemy"))
        self.player.change_HP(action_value)
