from Treengine.Game.SceneState import SceneState
from Treengine.Game.Spritesheet import SpriteSheet
import os


class PlayingState(SceneState):
    def __init__(self, scene):
        super().__init__("PlayingState", scene)

        self.charater_sheet = SpriteSheet(
            "MyGame\Resources\GameScene\kenney_pixelplatformer\Tilemap\\characters.png",
            16,
            1,
        )

        self.fist_tile = self.charater_sheet.get_tile(0, 0)

        # self.scene.add_renderable(self.fist_tile)

    pass

    def on_enter(self):
        print("PlayingState on_enter")
        super().on_enter()
        pass

    def on_exit(self):
        super().on_exit()
        pass

    def update(self, dt):
        super().update(dt)
        pass

    def handle_event(self, event):
        super().handle_event(event)
        pass

    def draw(self):
        super().draw()

    pass
