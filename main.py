from Treengine.Game.TreeGame import TreeGame

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