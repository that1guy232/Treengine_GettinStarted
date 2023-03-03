# Getting started.

[Click here for the link to the repository following this guide.](https://github.com/that1guy232/Treengine_GettinStarted)


This guide will help you get started with Treengine. It will cover the basics of the engine and how to use it to create a simple window

Are entry point will be the main.py file. This is where we will create our game instance and start the game loop.


### Main.py
```python

 '''
    First thing we need to do is import TreeGame from Treengine.Game.TreGame
    
    This instance will be used to create our game window and start the game loop
   
    It will also be used to manage our Game Scenes
    (If no scenes are added, the game will create a empty scene with nothing in it. More on this later)


 '''
from Treengine.Game.TreGame import TreeGame

def main():
    '''
        Create a new instance of TreeGame
        This will create a new window and start the game loop
    '''
    game = TreeGame()
    '''
        Start the game loop
        This will run until the game is closed
    '''
    game.run()
    pass

if __name__ == "__main__":
    main()
```

Now we have a window, but it's empty.

Let's add a scene to it.
Scenes are your game's levels. They can be menus, levels or just a splash screen. These will hold all of your game's entities and components and logic.

First let's create a main menu scene, we will call it MainMenuScene.py and place it in a folder following this:
```
    Root Folder
        |
        |---Treengine
        |---MyGame
        |   |
        |   |---Scenes
        |   |   |
        |   |   |---MainMenuScene
        |   |   |   |
        |   |   |   |---MainMenuScene.py
        |   |---Resources (More on this later)
        |---main.py
        
```
(This is just a convention, you can name your folders and files however you want, but it's recommended to keep things organized. I also plan on creating a editor to help with this among other things)

### MainMenuScene.py
________________________
```python
'''
    Fist thing, We import the GameScene class from Treengine.Game.GameScene
'''

from Treengine.Game.GameScene import GameScene

'''
    Next we create a class that inherits from GameScene
    This will allow us to create a new scene and add it to our game
'''

class MainMenuScene(GameScene):

        '''
         we take the Game as a parameter so we can access it's properties and methods we also initialize the super class with a name for our scene
        '''

    def __init__(self, game):
        # The name of the scene is important, it will be used to switch between scenes and to identify the scene
        super().__init__(game, "MainMenuScene")
        pass

    def on_enter(self):
        super().on_enter()
        pass

    def on_exit(self):
        super().on_exit()
        pass

    def update(self, delta_time):
        super().update(delta_time)
        pass

    def draw(self, screen):
        super().render(screen)
        pass

    def handle_events(self, events):
        super().handle_events(events)
        pass
```

Now that we have a scene, we need to add it to our game.
Back in our main.py file, we need to import our new scene and add it to our game. this can be done by adding the following lines of code to our main.py file.

### main.py
________________________
```python
from Treengine.Game.TreeGame import TreeGame

# Import our new scene
from MyGame.Scenes.MainMenuScene.MainMenuScene import MainMenuScene

def main():

    game = TreeGame()

    # add a new instance of our scene to the game
    game.add_scene(MainMenuScene(game))

    # This on it's own will not do anything, we need to switch to our new scene, this is were the name we gave our scene comes in handy
    game.switch_scene("MainMenuScene")

    game.run()

    pass


if __name__ == "__main__":
    main()
```

Now that's pretty boring, it's the same as before a empty scene. Let's add a background to it.
This will introduce us to basic rendering of Textures and objects.

For now are are game will be 800x600 pixels, so let's create a image that is 800x600 pixels and name it background.png and place it in the Resources folder under a Menu folder.
```
    |---Resources
    |   |---Menu
    |   |   |---background.png
```

Now we need to import the Texture class from ``Treengine.GameRenderer.Renderable``.

We will also need to import pygame so we can load our image.

### MainMenuScene.py
________________________
```python
# at the top of the file
import pygame
from Treengine.GameRenderer.Renderable import Texture

# now inside are constructor we have to load the assest it's self than create a new Texture object and pass it the loaded image
def __init__(self, game):
    super().__init__(game, "MainMenuScene")
    background_image = pygame.image.load("MyGame/Resources/Menu/background.png")
    
    # The texuture class has a few parameters, x, y, width, height, and image, It also has a optional visible parameter that is set to True by default
    self.background = Texture(0, 0, background_image.get_width(), background_image.get_height(), background_image)

    # we than append the texture to the scene's renderables list
    self.renderables.append(self.background)

    pass
```

The backgorund texture will now be rendered to the screen!

Let's add a exit button to our scene and a play button.

Continuing in are constructor we will add the following lines of code.

### MainMenuScene.py
________________________
```python
# import the button class from Treengine.UI at the top of your scene file
from Treengine.UI.Button import Button

# now back inside are constructor we will create a new exit button
self.exit_button = Button(0, 0, 100, 50, "Exit", game.quit)
# than we simply add it to the scene's UIWidgets list
self.add_UIWidget(self.exit_button)

# Now we have a function exit button. Let me explain a bit about the button before we move on.
# The button class takes 5 parameters, x, y, width, height, text, and a function to call when the button is clicked.
# so right now we are creating a button in the top left, with a width of 100 and a height of 50, with the text "Exit" and when it is clicked it will call the game.quit function(A function that is built into the game class that will close the application)

my_start_button = Button(
    100,
    0,
    100,
    50,
    (255, 0, 0),
    "Start",
    lambda: game.transition_to_scene("GameScene"),
) 

'''
Now we have a button that will change the scene to a scene called GameScene, If we do not have a scene called GameScene, it will throw an error when we try to switch to it.
The error will look something like this:

    ERROR: Scene not found
    Looking for scene: GameScene
    Available scenes:
    MainMenuScene
    
'''

```
