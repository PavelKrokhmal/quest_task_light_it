from actions.action_own_use import ActionOwnUse


class ActionController:
    @staticmethod
    def apply_action(player_from, player_to, action):
        action_value = action.get_random_value()

        if isinstance(action, ActionOwnUse):
            # Boundary HP correction
            delta_HP = player_from.init_HP - player_from.current_HP
            action_value = action_value if action_value <= delta_HP else delta_HP
            print("+{0} points HP for myself".format(action_value))
            player_from.change_HP(action_value)
        else:
            # ActionEnemy
            # Boundary HP correction
            action_value = (
                action_value
                if player_to.current_HP + action_value >= 0
                else -player_to.current_HP
            )
            print("{0} points HP for enemy".format(action_value))
            player_to.change_HP(action_value)
