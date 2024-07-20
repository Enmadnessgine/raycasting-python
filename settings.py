#game settings and constans
import math

#general
SCREEN_HEIGHT = 480
SCREEN_WIDTH = SCREEN_HEIGHT * 2
MAP_SIZE = 8
TILE_SIZE = int((SCREEN_WIDTH / 2) / MAP_SIZE)
MAX_DEPTH = int(MAP_SIZE * TILE_SIZE)

SCREEN_COLOR = 'BLACK'

FPS = 30

MAP = (
    '########'
    '#  #   #'
    '#  # ###'
    '#      #'
    '#      #'
    '#  ##  #'
    '#   #  #'
    '########'
)

#player
player_x = (SCREEN_WIDTH / 2) / 2
player_y = (SCREEN_WIDTH / 2) / 2
FOV = math.pi / 3
HALF_FOV = FOV / 2
player_angle = math.pi

#raycasting
CASTED_RAYS = 240
STEP_ANGLE = FOV / CASTED_RAYS
SCALE = (SCREEN_WIDTH / 2) / CASTED_RAYS
