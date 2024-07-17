import pygame

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Player properties
player_size = 20
player_x = 30
player_y = 30
player_speed = 3

# Maze properties
cell_size = 40
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

def is_wall(x, y):
    grid_x = x // cell_size
    grid_y = y // cell_size
    if 0 <= grid_x < 10 and 0 <= grid_y < 10:
        return maze[grid_y][grid_x] == 1
    return True

# Game loop
running = True
clock = pygame.time.Clock()

# Debug font
font = pygame.font.Font(None, 36)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move player
    keys = pygame.key.get_pressed()
    new_x, new_y = player_x, player_y
    moved = False
    if keys[pygame.K_LEFT]:
        new_x -= player_speed
        moved = True
    if keys[pygame.K_RIGHT]:
        new_x += player_speed
        moved = True
    if keys[pygame.K_UP]:
        new_y -= player_speed
        moved = True
    if keys[pygame.K_DOWN]:
        new_y += player_speed
        moved = True

    # Check for collisions (only check the center of the player)
    if not is_wall(new_x + player_size // 2, new_y + player_size // 2):
        player_x, player_y = new_x, new_y

    # Clear the screen
    screen.fill(WHITE)

    # Draw maze
    for y in range(10):
        for x in range(10):
            if maze[y][x] == 1:
                pygame.draw.rect(screen, BLACK, (x * cell_size, y * cell_size, cell_size, cell_size))

    # Draw player
    pygame.draw.rect(screen, RED, (player_x, player_y, player_size, player_size))

    # Debug info
    debug_text = font.render(f"X: {player_x}, Y: {player_y}, Moved: {moved}", True, BLACK)
    screen.blit(debug_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Control the game speed
    clock.tick(60)

pygame.quit()