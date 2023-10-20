import random

import pygame

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 10
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Initialize screen and clock
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paterson's Worms Visualizer")
clock = pygame.time.Clock()

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)
DIRECTIONS = [UP, DOWN, LEFT, RIGHT]

class Worm:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = random.choice(DIRECTIONS)
        self.grid = [[0 for _ in range(GRID_HEIGHT)] for _ in range(GRID_WIDTH)]
        self.grid[x][y] = 1

    def move(self):
        dx, dy = self.direction
        self.x += dx
        self.y += dy

        # Handle boundaries - wrapping around
        self.x %= GRID_WIDTH
        self.y %= GRID_HEIGHT

        if self.grid[self.x][self.y] == 0:
            directions = list(DIRECTIONS)
            directions.remove((-dx, -dy))  # Remove the opposite direction
            self.direction = random.choice(directions)
            self.grid[self.x][self.y] = 1

    def draw(self, screen):
        for x in range(GRID_WIDTH):
            for y in range(GRID_HEIGHT):
                if self.grid[x][y] == 1:
                    pygame.draw.rect(screen, RED, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def main():
    worm = Worm(GRID_WIDTH // 2, GRID_HEIGHT // 2)
    run = True
    move_worm = False

    while run:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    move_worm = True

        if move_worm:
            worm.move()
        worm.draw(screen)

        pygame.display.flip()
        clock.tick(10)

    pygame.quit()

if __name__ == "__main__":
    main()
