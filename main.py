from Treengine.Game.TreeGame import TreeGame

# import the main menu scene
from MyGame.Scenes.MainMenuScene.MainMenuScene import MainMenuScene

from MyGame.Scenes.PlayScene.PlayScene import PlayScene


def main():
    """
    Create a new instance of TreeGame
    This will create a new window and start the game loop
    """
    game = TreeGame()
    """
        Start the game loop
        This will run until the game is closed
    """

    # add the main menu scene
    game.add_scene(MainMenuScene(game))
    game.add_scene(PlayScene(game))

    # switch to the main menu scene right away
    game.transition_to_scene("MainMenuScene")

    game.run()
    pass


if __name__ == "__main__":
    main()
