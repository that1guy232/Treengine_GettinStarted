from Treengine.Game.SceneState import SceneState


class PlayingState(SceneState):
    def __init__(self, scene):
        super().__init__("PlayingState", scene)
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
