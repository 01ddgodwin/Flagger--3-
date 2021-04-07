import arcade
from game import constants
from game.level_1 import Level_1
from game.player import Player
from game.flagger import Flagger

setupShortcut = constants.SCREEN_HEIGHT, constants.SCREEN_WIDTH, constants.SCREEN_TITLE, constants.GRAVITY, constants.JUMP_SPEED, constants.MOVEMENT_SPEED, constants.RIGHT_MARGIN, constants.VIEWPORT_MARGIN, constants.GRID_PIXEL_SIZE, constants.SPRITE_PIXEL_SIZE


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """

        super().__init__(width, height, title)
        self.view_left = 0
        self.view_bottom = 0
        self.total_time = 0.0
        self.game_over = False


    def setup(self, setupShortcut):
        """ Set up the game and initialize the variables. """

        Level_1.setup(self)
        Player.on_draw(self)


        self.physics_engine = \
            arcade.PhysicsEnginePlatformer(self.player_sprite,
                                           self.all_wall_list,
                                           gravity_constant=constants.GRAVITY)

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)


    def on_key_press(self, key, modifiers):
        """
        Called whenever the mouse moves.
        """

        Flagger.on_key_press(self, key, modifiers)


    def on_key_release(self, key, modifiers):
        """
        Called when the user presses a mouse button.
        """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites
        self.physics_engine.update()

        # --- Manage Scrolling ---

        # Track if we need to change the viewport

        changed = False

        # Scroll left
        left_boundary = self.view_left + constants.VIEWPORT_MARGIN
        if self.player_sprite.left < left_boundary:
            self.view_left -= left_boundary - self.player_sprite.left
            changed = True

        # Scroll right
        right_boundary = self.view_left + constants.SCREEN_WIDTH - constants.RIGHT_MARGIN
        if self.player_sprite.right > right_boundary:
            self.view_left += self.player_sprite.right - right_boundary
            changed = True

        # Scroll up
        top_boundary = self.view_bottom + constants.SCREEN_HEIGHT - constants.VIEWPORT_MARGIN
        if self.player_sprite.top > top_boundary:
            self.view_bottom += self.player_sprite.top - top_boundary
            changed = True

        # Scroll down
        bottom_boundary = self.view_bottom + constants.VIEWPORT_MARGIN
        if self.player_sprite.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player_sprite.bottom
            changed = True

        # If we need to scroll, go ahead and do it.
        if changed:
            arcade.set_viewport(self.view_left,
                                constants.SCREEN_WIDTH + self.view_left,
                                self.view_bottom,
                                constants.SCREEN_HEIGHT + self.view_bottom)

        if int(self.total_time) % 60 == 60:
            self.game_over = TRUE

        # See if we get any flag
        flag_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                             self.flag_list)

        # Loop through each coin we hit (if any) and remove it
        for flag in flag_hit_list:
            # Remove the flag
            flag.remove_from_sprite_lists()

        if len(self.flag_list) == 0:
            self.game_over = TRUE
       

    def on_draw(self):
        arcade.start_render()
        self.static_wall_list.draw()
        self.moving_wall_list.draw()
        self.player_list.draw()
        self.flag_list.draw()

        # Calculate minutes
        minutes = int(self.total_time) // 60
        # Calculate seconds by using a modulus (remainder)
        seconds = int(self.total_time) % 60
        # Figure out our output
        output = f"Time: {minutes:02d}:{seconds:02d}"
        # Output the timer text.
        arcade.draw_text(output, self.view_left, self.view_bottom, arcade.color.WHITE, 20)

        goals = str("You have 60 seconds to get the 2 flags")
        arcade.draw_text(goals, self.view_left, self.view_bottom + 20, arcade.color.WHITE, 20)



def main():
    """ Main method """
    window = MyGame(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
    window.setup(setupShortcut)
    arcade.run()


if __name__ == "__main__":
    main()