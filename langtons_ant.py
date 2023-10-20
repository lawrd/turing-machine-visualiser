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
pygame.display.set_caption("Langton's Ant Visualizer")
clock = pygame.time.Clock()

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)
DIRECTIONS = [UP, RIGHT, DOWN, LEFT]  # Clockwise order

class LangtonsAnt:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction_index = 0  # Starts facing UP
        self.grid = [[0 for _ in range(GRID_HEIGHT)] for _ in range(GRID_WIDTH)]

    def move(self):
        # Get the next direction
        if self.grid[self.x][self.y] == 0:  # White cell
            self.direction_index = (self.direction_index + 1) % 4  # Turn clockwise
            self.grid[self.x][self.y] = 1  # Change to black
        else:  # Black cell
            self.direction_index = (self.direction_index - 1) % 4  # Turn counter-clockwise
            self.grid[self.x][self.y] = 0  # Change to white

        dx, dy = DIRECTIONS[self.direction_index]
        self.x += dx
        self.y += dy
        
        # Handle boundaries - wrapping around
        self.x %= GRID_WIDTH
        self.y %= GRID_HEIGHT

    def draw(self, screen):
        for x in range(GRID_WIDTH):
            for y in range(GRID_HEIGHT):
                color = BLACK if self.grid[x][y] == 1 else WHITE
                pygame.draw.rect(screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(screen, RED, (self.x * CELL_SIZE, self.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))  # Draw the ant

def main():
    ant = LangtonsAnt(GRID_WIDTH // 2, GRID_HEIGHT // 2)
    run = True
    move_ant = False

    while run:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    move_ant = True

        if move_ant:
            ant.move()
        ant.draw(screen)

        pygame.display.flip()
        clock.tick(10)

    pygame.quit()

if __name__ == "__main__":
    main()
