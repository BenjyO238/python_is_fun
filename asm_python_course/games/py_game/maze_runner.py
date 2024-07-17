import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Maze Runner")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Player properties
player_size = 20
player_x = player_size
player_y = player_size
player_speed = 3

# Maze properties
cell_size = 40
maze_width = WIDTH // cell_size
maze_height = HEIGHT // cell_size
maze = [[1 for _ in range(maze_width)] for _ in range(maze_height)]

# Simplified maze generation
for y in range(maze_height):
    for x in range(maze_width):
        if random.random() < 0.3:  # 30% chance of being a wall
            maze[y][x] = 1
        else:
            maze[y][x] = 0

# Ensure start and end are clear
maze[1][1] = 0
maze[maze_height-2][maze_width-2] = 0

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move player
    keys = pygame.key.get_pressed()
    new_x, new_y = player_x, player_y
    if keys[pygame.K_LEFT]:
        new_x -= player_speed
    if keys[pygame.K_RIGHT]:
        new_x += player_speed
    if keys[pygame.K_UP]:
        new_y -= player_speed
    if keys[pygame.K_DOWN]:
        new_y += player_speed

    # Simple collision detection
    cell_x = new_x // cell_size
    cell_y = new_y // cell_size
    if 0 <= cell_x < maze_width and 0 <= cell_y < maze_height:
        if maze[cell_y][cell_x] == 0:  # If the cell is empty
            player_x, player_y = new_x, new_y

    # Clear the screen
    screen.fill(WHITE)

    # Draw maze
    for y in range(maze_height):
        for x in range(maze_width):
            if maze[y][x] == 1:
                pygame.draw.rect(screen, BLACK, (x * cell_size, y * cell_size, cell_size, cell_size))

    # Draw player
    pygame.draw.rect(screen, RED, (player_x, player_y, player_size, player_size))

    # Draw start and end points
    pygame.draw.rect(screen, GREEN, (cell_size, cell_size, cell_size, cell_size))
    pygame.draw.rect(screen, GREEN, ((maze_width-2) * cell_size, (maze_height-2) * cell_size, cell_size, cell_size))

    # Update the display
    pygame.display.flip()

    # Control the game speed
    clock.tick(60)

pygame.quit()