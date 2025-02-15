import pygame, random, math

pygame.init()

FPS = 60

HEIGHT, WIDTH = 800, 800
ROWS = 4
COLS = 4

RECT_HEIGHT = HEIGHT // ROWS
RECT_WIDTH = WIDTH // COLS

OUTLINE_COLOUR = (187, 173, 160)
OUTLINE_THICKNESS = 10
BACKGROUND_COLOUR = (205, 192, 180)
FONT_COLOUR = (119, 110, 101)

WINDOW = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption("2048")

FONT = pygame.font.SysFont("comicsans", 60, bold=True)
MOVE_VEL = 20