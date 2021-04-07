import arcade 
from game import constants

class Level_2(arcade.Sprite):
    def __init__(self):
        # Create floor
        self.static_wall_list = None
        self.moving_wall_list = None
        self.all_wall_list = None
        self.player_list = None

    def setup(self):

        # Sprite lists
        arcade.play_sound(constants.BACKGROUND_MUSIC)
        self.all_wall_list = arcade.SpriteList()
        self.static_wall_list = arcade.SpriteList()
        self.moving_wall_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/male_adventurer/maleAdventurer_idle.png", constants.SPRITE_SCALING)
        self.player_sprite.center_x = 2 * constants.GRID_PIXEL_SIZE
        self.player_sprite.center_y = 3 * constants.GRID_PIXEL_SIZE
        self.player_list.append(self.player_sprite)

        #PATH 2
        #PLATFORM 1

        wall = arcade.Sprite(constants.PLATFORM_IMAGE, constants.SPRITE_SCALING)
        wall.center_y = 7 * constants.GRID_PIXEL_SIZE
        wall.center_x = 18 * constants.GRID_PIXEL_SIZE

        self.all_wall_list.append(wall)
        self.static_wall_list.append(wall)


        #PLATFORM 2
        wall = arcade.Sprite(constants.PLATFORM_IMAGE, constants.SPRITE_SCALING)     
        wall.center_y = 8 * constants.GRID_PIXEL_SIZE
        wall.center_x = 24 * constants.GRID_PIXEL_SIZE

        self.all_wall_list.append(wall)
        self.static_wall_list.append(wall)

        #PLATFORM 3
        wall = arcade.Sprite(constants.PLATFORM_IMAGE, constants.SPRITE_SCALING)     
        wall.center_y = 9 * constants.GRID_PIXEL_SIZE
        wall.center_x = 30 * constants.GRID_PIXEL_SIZE

        self.all_wall_list.append(wall)
        self.static_wall_list.append(wall)

        #PLATFORM 4
        wall = arcade.Sprite(constants.PLATFORM_IMAGE, constants.SPRITE_SCALING)     
        wall.center_y = 10 * constants.GRID_PIXEL_SIZE
        wall.center_x = 36 * constants.GRID_PIXEL_SIZE

        self.all_wall_list.append(wall)
        self.static_wall_list.append(wall)

        #PLATFORM 5
        wall = arcade.Sprite(constants.PLATFORM_IMAGE , constants.SPRITE_SCALING)
        wall.center_y = 10 * constants.GRID_PIXEL_SIZE
        wall.center_x = 40 * constants.GRID_PIXEL_SIZE
        wall.boundary_top = 18 * constants.GRID_PIXEL_SIZE
        wall.boundary_bottom = 8 * constants.GRID_PIXEL_SIZE
        wall.change_y = 3 * constants.SPRITE_SCALING

        self.all_wall_list.append(wall)
        self.moving_wall_list.append(wall)


        #PLATFORM 6
        wall = arcade.Sprite(constants.PLATFORM_IMAGE , constants.SPRITE_SCALING)     
        wall.center_y = 17 * constants.GRID_PIXEL_SIZE
        wall.center_x = 36 * constants.GRID_PIXEL_SIZE

        self.all_wall_list.append(wall)
        self.static_wall_list.append(wall)

        #PLATFORM 7
        wall = arcade.Sprite(constants.PLATFORM_IMAGE, constants.SPRITE_SCALING)     
        wall.center_y = 16 * constants.GRID_PIXEL_SIZE
        wall.center_x = 30 * constants.GRID_PIXEL_SIZE

        self.all_wall_list.append(wall)
        self.static_wall_list.append(wall)


        #PLATFORM 8
        wall = arcade.Sprite(constants.PLATFORM_IMAGE, constants.SPRITE_SCALING)     
        wall.center_y = 15 * constants.GRID_PIXEL_SIZE
        wall.center_x = 24 * constants.GRID_PIXEL_SIZE

        self.all_wall_list.append(wall)
        self.static_wall_list.append(wall)

        arcade.start_render()

        # Draw the sprites.
        self.static_wall_list.draw()
        self.moving_wall_list.draw()
        self.player_list.draw()