import os

from actions.kit import LowDamage, HightDamage, Healing
from player import Player
from controllers import GameController, PlayerController, BotController

if __name__ == "__main__":

    # PLAYER

    player1_controller = PlayerController(
        Player("Player", 100), [LowDamage(), HightDamage(), Healing()]
    )

    # BOT

    player2_controller = BotController(
        Player("Computer", 100), [LowDamage(), HightDamage(), Healing()]
    )

    gameController = GameController(player1_controller, player2_controller)

    print("This's a simple game for quest Light IT")

    if input("Press <Enter> to continue or any other for exit:") == "":
        while True:
            gameController.play()
            if input("Press <y> to restart or any other for exit:") == "y":
                gameController.restart()
                os.system("cls")
            else:
                break
    print("Exit...")
