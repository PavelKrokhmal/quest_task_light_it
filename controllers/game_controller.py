from balancer import Balancer
from .action_controller import ActionController

from actions.action_own_use import ActionOwnUse


class GameController:
    def __init__(self, player1_controller, player2_controller):
        self.player1_controller = player1_controller
        self.player2_controller = player2_controller
        self.balancer = Balancer(player1_controller, player2_controller)

    def get_formated_players_status(self):
        return "|> {0} <vs> {1} <|".format(
            self.player1_controller.player, self.player2_controller.player
        )

    def get_formated_player_status(self, player):
        return "|> NOW TURN {0}".format(player)

    def get_formated_winer(self, player):
        return "\nWINNER ===== {0} ======\n".format(player)

    def restart(self):
        self.player1_controller.player.reset()
        self.player2_controller.player.reset()
        self.balancer.reset()

    def play(self):

        while True:
            print(self.get_formated_players_status())

            (
                first_player_controller,
                second_player_controller,
            ) = self.balancer.get_battle_pair()

            print(self.get_formated_player_status(first_player_controller.player))

            selected_action = first_player_controller.get_selected_action()

            ActionController.apply_action(
                first_player_controller.player,
                second_player_controller.player,
                selected_action,
            )

            if not second_player_controller.player.is_alive():
                print(self.get_formated_winer(first_player_controller.player))
                break
            print("\n")
