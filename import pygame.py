import pygame
import random

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLOCK_SIZE = 30
GRID_WIDTH = 10
GRID_HEIGHT = 20
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)

# Tetromino shapes
SHAPES = [
    [[1, 1, 1, 1]],                             # I
    [[1, 1, 1], [0, 1, 0]],                     # T
    [[1, 1, 1], [1, 0, 0]],                     # L
    [[1, 1, 1], [0, 0, 1]],                     # J
    [[1, 1], [1, 1]],                           # O
    [[1, 1, 0], [0, 1, 1]],                     # S
    [[0, 1, 1], [1, 1, 0]]                      # Z
]

SHAPES_COLORS = [RED, GREEN, BLUE, CYAN, MAGENTA, YELLOW, ORANGE]

class Tetris:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Tetris")
        self.clock = pygame.time.Clock()
        self.grid = [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]
        self.current_piece = self.new_piece()
        self.game_over = False

    def new_piece(self):
        shape = random.choice(SHAPES)
        color = random.choice(SHAPES_COLORS)
        piece = {
            "shape": shape,
            "color": color,
            "x": GRID_WIDTH // 2 - len(shape[0]) // 2,
            "y": 0
        }
        return piece

    def check_collision(self):
        shape = self.current_piece["shape"]
        x, y = self.current_piece["x"], self.current_piece["y"]
        for i in range(len(shape)):
            for j in range(len(shape[i])):
                if shape[i][j] and (x + j < 0 or x + j >= GRID_WIDTH or y + i >= GRID_HEIGHT or self.grid[y + i][x + j]):
                    return True
        return False

    def merge_piece(self):
        shape = self.current_piece["shape"]
        x, y = self.current_piece["x"], self.current_piece["y"]
        for i in range(len(shape)):
            for j in range(len(shape[i])):
                if shape[i][j]:
                    self.grid[y + i][x + j] = self.current_piece["color"]

    def remove_completed_lines(self):
        lines_to_remove = [i for i, row in enumerate(self.grid) if all(row)]
        for line in lines_to_remove:
            del self.grid[line]
            self.grid.insert(0, [0] * GRID_WIDTH)

    def draw_grid(self):
        for i in range(GRID_HEIGHT):
            for j in range(GRID_WIDTH):
                if self.grid[i][j]:
                    pygame.draw.rect(self.screen, self.grid[i][j], (j * BLOCK_SIZE, i * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

    def draw_piece(self):
        shape = self.current_piece["shape"]
        x, y = self.current_piece["x"], self.current_piece["y"]
        color = self.current_piece["color"]
        for i in range(len(shape)):
            for j in range(len(shape[i])):
                if shape[i][j]:
                    pygame.draw.rect(self.screen, color, ((x + j) * BLOCK_SIZE, (y + i) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

    def move_piece_down(self):
        self.current_piece["y"] += 1
        if self.check_collision():
            self.current_piece["y"] -= 1
            self.merge_piece()
            self.remove_completed_lines()
            self.current_piece = self.new_piece()
            if self.check_collision():
                self.game_over = True

    def move_piece_sideways(self, dx):
        self.current_piece["x"] += dx
        if self.check_collision():
            self.current_piece["x"] -= dx

    def rotate_piece(self):
        shape = self.current_piece["shape"]
        size = len(shape)
        rotated_shape = [[0] * size for _ in range(size)]
        for i in range(size):
            for j in range(size):
                rotated_shape[i][j] = shape[size - j - 1][i]
        self.current_piece["shape"] = rotated_shape
        if self.check_collision():
            self.current_piece["shape"] = shape

    def run(self):
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.move_piece_sideways(-1)
                    if event.key == pygame.K_RIGHT:
                        self.move_piece_sideways(1)
                    if event.key == pygame.K_DOWN:
                        self.move_piece_down()
                    if event.key == pygame.K_UP:
                        self.rotate_piece()

            self.screen.fill(BLACK)
            self.move_piece_down()
            self.draw_grid()
            self.draw_piece()
            pygame.display.flip()
            self.clock.tick(10)

        pygame.quit()

if __name__ == "__main__":
    Tetris().run()
