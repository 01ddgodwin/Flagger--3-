# This is a test for our real project.

#JOSPEH'S DEMO

import arcade
from game import constants

SPRITE_SCALING = 0.5
SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 900
SCREEN_TITLE = "Sprite with Moving Platforms Example"
SPRITE_PIXEL_SIZE = 128
GRID_PIXEL_SIZE = (SPRITE_PIXEL_SIZE * SPRITE_SCALING)

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
VIEWPORT_MARGIN = 4*SPRITE_PIXEL_SIZE * SPRITE_SCALING
RIGHT_MARGIN = 4 * SPRITE_PIXEL_SIZE * SPRITE_SCALING

#BLAKE'S VIEWPOINT IDEA
# VIEWPORT_MARGIN = SPRITE_PIXEL_SIZE * SPRITE_SCALING
# RIGHT_MARGIN = 7 * SPRITE_PIXEL_SIZE * SPRITE_SCALING
# LEFT_MARGIN = 5 * SPRITE_PIXEL_SIZE * SPRITE_SCALING

# Physics
MOVEMENT_SPEED = 13 * SPRITE_SCALING
JUMP_SPEED = 40 * SPRITE_SCALING
GRAVITY = 1 * SPRITE_SCALING


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """

        super().__init__(width, height, title)

        # Sprite lists

        # We use an all-wall list to check for collisions.
        self.all_wall_list = None

        # Drawing non-moving walls separate from moving walls improves performance.
        self.static_wall_list = None
        self.moving_wall_list = None

        self.player_list = None

        # Set up the player
        self.player_sprite = None
        self.physics_engine = None
        self.view_left = 0
        self.view_bottom = 0
        self.end_of_map = 0
        self.game_over = False


    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        arcade.play_sound(constants.BACKGROUND_MUSIC)
        self.all_wall_list = arcade.SpriteList()
        self.static_wall_list = arcade.SpriteList()
        self.moving_wall_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/male_adventurer/maleAdventurer_idle.png", SPRITE_SCALING)
        self.player_sprite.center_x = 2 * GRID_PIXEL_SIZE
        self.player_sprite.center_y = 3 * GRID_PIXEL_SIZE
        self.player_list.append(self.player_sprite)

        # Create floor
        for i in range(50):
            wall = arcade.Sprite(":resources:images/tiles/bridgeB.png", SPRITE_SCALING)
            wall.bottom = 0
            wall.center_x = i * GRID_PIXEL_SIZE
            self.static_wall_list.append(wall)
            self.all_wall_list.append(wall)


        #Create platform 1

        for i in range(11, 14):
            wall = arcade.Sprite(":resources:images/tiles/dirtHalf_mid.png", SPRITE_SCALING)
            wall.center_y = 4 * GRID_PIXEL_SIZE
            wall.center_x = i * GRID_PIXEL_SIZE

            self.all_wall_list.append(wall)
            self.static_wall_list.append(wall)   

        #Platform 1 Edges

        wall = arcade.Sprite(":resources:images/tiles/dirtHalf_left.png", SPRITE_SCALING)
        wall.center_y = 4 * GRID_PIXEL_SIZE
        wall.center_x = 10 * GRID_PIXEL_SIZE

        self.all_wall_list.append(wall)
        self.static_wall_list.append(wall)

        wall = arcade.Sprite(":resources:images/tiles/dirtHalf_right.png", SPRITE_SCALING)
        wall.center_y = 4 * GRID_PIXEL_SIZE
        wall.center_x = 14 * GRID_PIXEL_SIZE

        self.all_wall_list.append(wall)
        self.static_wall_list.append(wall) 

        # Create platform 2 (MOVES DIAGONAL)
        wall = arcade.Sprite(":resources:images/tiles/dirtHalf.png", SPRITE_SCALING)
        wall.center_y = 6 * GRID_PIXEL_SIZE
        wall.center_x = 6 * GRID_PIXEL_SIZE
        wall.boundary_right = 8 * GRID_PIXEL_SIZE
        wall.boundary_left = 4 * GRID_PIXEL_SIZE
        wall.boundary_top = 8 * GRID_PIXEL_SIZE
        wall.boundary_bottom = 4 * GRID_PIXEL_SIZE
        wall.change_x = 3 * SPRITE_SCALING
        wall.change_y = 3 * SPRITE_SCALING

        self.all_wall_list.append(wall)
        self.moving_wall_list.append(wall)


        #CREATE PLATFORM 3

        for i in range(1, 3):
            wall = arcade.Sprite(":resources:images/tiles/dirtHalf_mid.png", SPRITE_SCALING)
            wall.center_y = 9 * GRID_PIXEL_SIZE
            wall.center_x = i * GRID_PIXEL_SIZE

            self.all_wall_list.append(wall)
            self.static_wall_list.append(wall)    

        #Platform 3 Edges

        wall = arcade.Sprite(":resources:images/tiles/dirtHalf_left.png", SPRITE_SCALING)
        wall.center_y = 9 * GRID_PIXEL_SIZE
        wall.center_x = 0 * GRID_PIXEL_SIZE

        self.all_wall_list.append(wall)
        self.static_wall_list.append(wall)

        wall = arcade.Sprite(":resources:images/tiles/dirtHalf_right.png", SPRITE_SCALING)
        wall.center_y = 9 * GRID_PIXEL_SIZE
        wall.center_x = 3 * GRID_PIXEL_SIZE

        self.all_wall_list.append(wall)
        self.static_wall_list.append(wall) 

        #CREATE PLATFORM 4
        wall = arcade.Sprite(":resources:images/tiles/dirthalf.png", SPRITE_SCALING)
        wall.center_y = 12 * GRID_PIXEL_SIZE
        wall.center_x = -3 * GRID_PIXEL_SIZE

        self.all_wall_list.append(wall)
        self.static_wall_list.append(wall)

        #Create platform 5

        for i in range(1, 3):
            wall = arcade.Sprite(":resources:images/tiles/dirtHalf_mid.png", SPRITE_SCALING)
            wall.center_y = 15 * GRID_PIXEL_SIZE
            wall.center_x = i * GRID_PIXEL_SIZE

            self.all_wall_list.append(wall)
            self.static_wall_list.append(wall)  
        
        wall = arcade.Sprite(":resources:images/tiles/dirtHalf_left.png", SPRITE_SCALING)
        wall.center_y = 15 * GRID_PIXEL_SIZE
        wall.center_x = 0 * GRID_PIXEL_SIZE

        self.all_wall_list.append(wall)
        self.static_wall_list.append(wall)

        wall = arcade.Sprite(":resources:images/tiles/dirtHalf_right.png", SPRITE_SCALING)
        wall.center_y = 15 * GRID_PIXEL_SIZE
        wall.center_x = 3 * GRID_PIXEL_SIZE

        self.all_wall_list.append(wall)
        self.static_wall_list.append(wall) 

        #Create platform 6

        wall = arcade.Sprite(":resources:images/tiles/dirtCenter_rounded.png", SPRITE_SCALING)
        wall.center_y = 9 * GRID_PIXEL_SIZE
        wall.center_x = 9 * GRID_PIXEL_SIZE
        wall.boundary_top = 17 * GRID_PIXEL_SIZE
        wall.boundary_bottom = 12 * GRID_PIXEL_SIZE
        wall.change_y = 3 * SPRITE_SCALING

        self.all_wall_list.append(wall)
        self.moving_wall_list.append(wall)
        


        #Create platform 7

        for i in range(15, 19):
            wall = arcade.Sprite(":resources:images/tiles/dirtCenter_rounded.png", SPRITE_SCALING)
            wall.center_y = 17 * GRID_PIXEL_SIZE
            wall.center_x = i * GRID_PIXEL_SIZE

            self.all_wall_list.append(wall)
            self.static_wall_list.append(wall) 


        #PATH 2
        #PLATFORM 1
        wall.center_y = 7 * GRID_PIXEL_SIZE
        wall.center_x = 18 * GRID_PIXEL_SIZE

        self.all_wall_list.append(wall)
        self.static_wall_list.append(wall)


        #PLATFORM 2
        wall = arcade.Sprite(":resources:images/tiles/dirtCenter_rounded.png", SPRITE_SCALING)     
        wall.center_y = 8 * GRID_PIXEL_SIZE
        wall.center_x = 24 * GRID_PIXEL_SIZE

        self.all_wall_list.append(wall)
        self.static_wall_list.append(wall)

        #PLATFORM 3
        wall = arcade.Sprite(":resources:images/tiles/dirtCenter_rounded.png", SPRITE_SCALING)     
        wall.center_y = 9 * GRID_PIXEL_SIZE
        wall.center_x = 30 * GRID_PIXEL_SIZE

        self.all_wall_list.append(wall)
        self.static_wall_list.append(wall)

        #PLATFORM 4
        wall = arcade.Sprite(":resources:images/tiles/dirtCenter_rounded.png", SPRITE_SCALING)     
        wall.center_y = 10 * GRID_PIXEL_SIZE
        wall.center_x = 36 * GRID_PIXEL_SIZE

        self.all_wall_list.append(wall)
        self.static_wall_list.append(wall)

        #PLATFORM 5
        wall = arcade.Sprite(":resources:images/tiles/dirtCenter_rounded.png", SPRITE_SCALING)
        wall.center_y = 10 * GRID_PIXEL_SIZE
        wall.center_x = 40 * GRID_PIXEL_SIZE
        wall.boundary_top = 18 * GRID_PIXEL_SIZE
        wall.boundary_bottom = 8 * GRID_PIXEL_SIZE
        wall.change_y = 3 * SPRITE_SCALING

        self.all_wall_list.append(wall)
        self.moving_wall_list.append(wall)


        #PLATFORM 6
        wall = arcade.Sprite(":resources:images/tiles/dirtCenter_rounded.png", SPRITE_SCALING)     
        wall.center_y = 17 * GRID_PIXEL_SIZE
        wall.center_x = 36 * GRID_PIXEL_SIZE

        self.all_wall_list.append(wall)
        self.static_wall_list.append(wall)

        #PLATFORM 7
        wall = arcade.Sprite(":resources:images/tiles/dirtCenter_rounded.png", SPRITE_SCALING)     
        wall.center_y = 16 * GRID_PIXEL_SIZE
        wall.center_x = 24 * GRID_PIXEL_SIZE

        self.all_wall_list.append(wall)
        self.static_wall_list.append(wall)

        #PLATFORM 8
        wall = arcade.Sprite(":resources:images/tiles/dirtCenter_rounded.png", SPRITE_SCALING)     
        wall.center_y = 14 * GRID_PIXEL_SIZE
        wall.center_x = 18 * GRID_PIXEL_SIZE

        self.all_wall_list.append(wall)
        self.static_wall_list.append(wall)


        #GOAL *I put a platform, lets find a way to do it better"

        wall = arcade.Sprite(":resources:images/items/flagRed1.png", SPRITE_SCALING)
        wall.center_y = 18 * GRID_PIXEL_SIZE
        wall.center_x = 17 * GRID_PIXEL_SIZE
        
        self.all_wall_list.append(wall)
        self.static_wall_list.append(wall)


        self.physics_engine = \
            arcade.PhysicsEnginePlatformer(self.player_sprite,
                                           self.all_wall_list,
                                           gravity_constant=GRAVITY)

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

        # Set the viewport boundaries
        # These numbers set where we have 'scrolled' to.
        self.view_left = 0
        self.view_bottom = 0

        self.game_over = False

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw the sprites.
        self.static_wall_list.draw()
        self.moving_wall_list.draw()
        self.player_list.draw()

        # Put the text on the screen.
        # Adjust the text position based on the viewport so that we don't
        # scroll the text too.
        distance = self.player_sprite.right
        output = f"Distance: {distance}"
        arcade.draw_text(output, self.view_left + 10, self.view_bottom + 20,
                         arcade.color.WHITE, 14)

    def on_key_press(self, key, modifiers):
        """
        Called whenever the mouse moves.
        """
        if key == arcade.key.UP:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = JUMP_SPEED
                arcade.play_sound(constants.JUMP_SOUND)
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

        #ADDED to restart the game.
        elif key == arcade.key.ESCAPE:
            self.setup()


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
        left_boundary = self.view_left + VIEWPORT_MARGIN
        if self.player_sprite.left < left_boundary:
            self.view_left -= left_boundary - self.player_sprite.left
            changed = True

        # Scroll right
        right_boundary = self.view_left + SCREEN_WIDTH - RIGHT_MARGIN
        if self.player_sprite.right > right_boundary:
            self.view_left += self.player_sprite.right - right_boundary
            changed = True

        # Scroll up
        top_boundary = self.view_bottom + SCREEN_HEIGHT - VIEWPORT_MARGIN
        if self.player_sprite.top > top_boundary:
            self.view_bottom += self.player_sprite.top - top_boundary
            changed = True

        # Scroll down
        bottom_boundary = self.view_bottom + VIEWPORT_MARGIN
        if self.player_sprite.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player_sprite.bottom
            changed = True

        # If we need to scroll, go ahead and do it.
        if changed:
            arcade.set_viewport(self.view_left,
                                SCREEN_WIDTH + self.view_left,
                                self.view_bottom,
                                SCREEN_HEIGHT + self.view_bottom)


def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()