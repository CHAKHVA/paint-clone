from pygame import font

NAME = 'Paint'

FPS = 120

# Screen Resolution
WIDTH = 1200
HEIGHT = 900

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255,165,0)
BROWN = (139,69,19)
PURPLE = (128,0,128)

BACKGROUND_COLOR = WHITE

def init_font(size):
    return font.SysFont("Verdana", size)