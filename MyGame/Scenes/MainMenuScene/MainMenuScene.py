from Treengine.Game.GameScene import GameScene
from Treengine.GameRenderer.Renderable import Texture
from Treengine.UI.Button import Button

import pygame


class MainMenuScene(GameScene):
    def __init__(self, game) -> None:
        super().__init__(game, "MainMenuScene")

        background_image = pygame.image.load("MyGame/Resources/Menu/background.png")

        my_exit_button = Button(
            400,
            400,
            100,
            50,
            (255, 0, 0),
            "Exit",
            game.quit,
            
        )

        self.add_UIWidget(my_exit_button)

        my_start_button = Button(
            200,
            400,
            100,
            50,
            (255, 0, 0),
            "Start",
            lambda: game.transition_to_scene("GameScene"),
        )

        self.add_UIWidget(my_start_button)

        self.background = Texture(
            0,
            0,
            background_image.get_width(),
            background_image.get_height(),
            background_image,
        )

        self.add_renderable(self.background)

        pass

    pass
