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

FONT = pygame.font.SysFont("comicsans", 60, bold=True)
MOVE_VEL = 20

WINDOW = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption("2048")

class Tile:
    COLOURS = [
        (237, 229, 218),
        (238, 225, 201),
        (243, 178, 122),
        (246, 150, 101),
        (247, 124, 95),
        (247, 95, 59),
        (237, 208, 115),
        (237, 204, 99),
        (236, 80, 202),
    ]

    def __init__(self, value, row, col):
        self.value = value
        self.row = row
        self.col = col
        self.x = col * RECT_WIDTH
        self.y = row * RECT_HEIGHT

    def get_colour(self):
        colour_index = int(math.log2(self.value)) - 1
        colour = self.COLOURS[colour_index]
        return colour

    def draw(self, window):
        colour = self.get_colour()
        pygame.draw.rect(window, colour, (self.x, self.y, RECT_HEIGHT, RECT_WIDTH))

        text = FONT.render(str(self.value), 1, FONT_COLOUR)
        window.blit(
            text,
            (
                self.x + (RECT_WIDTH / 2 - text.get_width() / 2),
                self.y + (RECT_HEIGHT / 2 - text.get_height() / 2),
            ),
        )
        
    def move(self, delta):
        pass

    def set_pos(self):
        pass



def draw_grid(window):
    for row in range(1, ROWS):
        y = row * RECT_HEIGHT
        pygame.draw.line(window, OUTLINE_COLOUR, (0, y), (WIDTH, y), OUTLINE_THICKNESS)

    for col in range(1, COLS):
        x = col * RECT_WIDTH
        pygame.draw.line(window, OUTLINE_COLOUR, (x, 0), (x, HEIGHT), OUTLINE_THICKNESS)

    pygame.draw.rect(window, OUTLINE_COLOUR, (0, 0, HEIGHT, WIDTH), OUTLINE_THICKNESS)

def draw(window, tiles):
    window.fill(BACKGROUND_COLOUR)

    for tile in tiles.values():
        tile.draw(window)

    draw_grid(window)

    pygame.display.update()

def get_random_pos(tiles):
    col = None
    row = None

    while True:
        col = random.randrange(0, COLS)
        row = random.randrange(0, ROWS)

        if f"{row}{col}" not in tiles:
            break

def generate_tiles():
    tiles = {}
    for _ in range(2):
        row, col = get_random_pos(tiles)
        tiles[f"{row}{col}"] = Tile(2, row, col)

    return tiles

def main(window):
    clock = pygame.time.Clock()
    run = True

    tiles = {}

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        draw(window, tiles)

    pygame.quit()

if __name__ == "__main__":
    main(WINDOW)