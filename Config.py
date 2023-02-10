from enum import Enum


# Level
class GameLevel(Enum):
    EASY = 1,
    MEDIUM = 2,
    HARD = 3


# Colors
class Colors():
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 50, 50)
    YELLOW = (255, 255, 0)
    GREEN = (0, 255, 50)
    BLUE = (50, 50, 255)
    GREY = (200, 200, 200)
    ORANGE = (200, 100, 50)
    CYAN = (0, 255, 255)
    MAGENTA = (255, 0, 255)
    TRANS = (1, 1, 1)
    SKY = (92, 148, 252)


# By Level
def get_time_by_level(level):
    if level == GameLevel.EASY:
        return 120
    elif level == GameLevel.HARD:
        return 30
    else:
        return 60


def get_max_targets_by_level(level):
    if level == GameLevel.EASY:
        return 15
    elif level == GameLevel.HARD:
        return 5
    else:
        return 10


def get_speed_by_level(level):
    if level == GameLevel.EASY:
        return -1, -0.5
    elif level == GameLevel.HARD:
        return -2, -1.5
    else:
        return -1.5, -1


# Config
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 400
FPS = 60
LEVEL = GameLevel.MEDIUM
PLAYER_BALL_RADIUS = 10
PLAYER_BALL_COLOR = Colors.RED
TARGET_BALL_RADIUS = 20
TARGET_BALL_COLOR = Colors.YELLOW
MAX_TARGETS = get_max_targets_by_level
TIME = get_time_by_level

# Player physics
GRAVITY = 0.0005
SPEED_INCREASE_RATE = 0.038
SPEED_DECREASE_RATE = 0.038
FALL_MULTIPLIER = 2.0
MIN_MOVE_SPEED = lambda level: get_speed_by_level(level)[0]
MAX_MOVE_SPEED = lambda level: get_speed_by_level(level)[1]
MIN_FALL_SPEED = -0.5
MAX_FALL_SPEED = -0.1
CANNON_FIREPOWER = 150
MASS = 20
