import ctypes

user32 = ctypes.windll.user32
screen_width = user32.GetSystemMetrics(0)
screen_height = user32.GetSystemMetrics(1)

DEFAULT_WIDTH = screen_height / 2
DEFAULT_HEIGHT = screen_height - 100
WIDTH = DEFAULT_WIDTH
HEIGHT = DEFAULT_HEIGHT

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)