import arcade
from game import constants
from game.player import Player
from game.flagger import Flagger


setupShortcut = constants.SCREEN_HEIGHT, constants.SCREEN_WIDTH, constants.SCREEN_TITLE, constants.GRAVITY, constants.JUMP_SPEED, constants.MOVEMENT_SPEED, constants.RIGHT_MARGIN, constants.VIEWPORT_MARGIN, constants.GRID_PIXEL_SIZE, constants.SPRITE_PIXEL_SIZE

def main():
    """ Main method """

    # create the cast {key: tag, value: list}
    cast = {}
    
    player = Player()
    cast["player"] = [player]

    # create the script {key: tag, value: list}
    script = {}


    flagger = Flagger(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
    flagger.setup(setupShortcut)
    arcade.run()
  

if __name__ == "__main__":
    main()