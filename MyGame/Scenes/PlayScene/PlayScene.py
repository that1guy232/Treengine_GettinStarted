from Treengine.Game.GameScene import GameScene
from MyGame.Scenes.PlayScene.PlayingState import PlayingState


class PlayScene(GameScene):
    def __init__(self, game):
        super().__init__(game, "PlayScene")

        self.playingState = PlayingState(self)

        pass

    def on_enter(self):
        print("PlayScene on_enter")
        super().on_enter()
        self.state_machine.push_state(self.playingState)
        pass

    def on_exit(self):
        super().on_exit()
        pass

    def update(self, dt):
        super().update(dt)
        pass

    def draw(self):
        super().draw()
        pass

    def handle_event(self, event):
        super().handle_event(event)
        pass

    pass
