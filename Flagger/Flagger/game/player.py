import arcade
from game import constants

class Player(arcade.Sprite):
    def __init__(self):

        self.player_sprite = None
        self.player_sprite = None
        self.physics_engine = None
        self.view_left = 0
        self.view_bottom = 0
        self.end_of_map = 0
        self.game_over = False

        self.player_list = None
        # super().__init__(constants.PLAYER_IMAGE, constants.SPRITE_SCALING)

        self.player_sprite.center_x = 2 * constants.GRID_PIXEL_SIZE
        self.player_sprite.center_y = 3 * constants.GRID_PIXEL_SIZE
        self.player_list.append(self.player_sprite)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        # arcade.start_render()

        # # Draw the sprites.
        # self.static_wall_list.draw()
        # self.moving_wall_list.draw()
        self.player_list.draw()

        # Put the text on the screen.
        # Adjust the text position based on the viewport so that we don't
        # scroll the text too.
        distance = self.player_sprite.right
        output = f"Distance: {distance}"
        arcade.draw_text(output, self.view_left + 10, self.view_bottom + 20,
                         arcade.color.WHITE, 14)