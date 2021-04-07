import arcade

# Sprite Measurments 
SPRITE_SCALING = 0.5
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Flagger"
SPRITE_PIXEL_SIZE = 128
GRID_PIXEL_SIZE = (SPRITE_PIXEL_SIZE * SPRITE_SCALING)

# Viewpoints Placement
VIEWPORT_MARGIN = 4*SPRITE_PIXEL_SIZE * SPRITE_SCALING
RIGHT_MARGIN = 4 * SPRITE_PIXEL_SIZE * SPRITE_SCALING

#BLAKE'S VIEWPOINT IDEA
# VIEWPORT_MARGIN = SPRITE_PIXEL_SIZE * SPRITE_SCALING
# RIGHT_MARGIN = 7 * SPRITE_PIXEL_SIZE * SPRITE_SCALING
# LEFT_MARGIN = 5 * SPRITE_PIXEL_SIZE * SPRITE_SCALING

# Physics
MOVEMENT_SPEED = 12 * SPRITE_SCALING
JUMP_SPEED = 35 * SPRITE_SCALING
GRAVITY = 1 * SPRITE_SCALING
UPDATES_PER_FRAME = 5
RIGHT_FACING = 0
LEFT_FACING = 1

# Sprite Images
PLAYER_IMAGE = ":resources:images/animated_characters/male_adventurer/maleAdventurer_idle.png"
FLAG_IMAGE = ":resources:images/items/flagRed1.png"
FLOOR_IMAGE = ":resources:images/tiles/bridgeB.png"
PLATFORM_IMAGE = ":resources:images/tiles/dirtHalf.png"


# Sounds
JUMP_SOUND = arcade.load_sound(":resources:sounds/jump2.wav")
BACKGROUND_MUSIC = arcade.load_sound("game/assets/music.mp3")