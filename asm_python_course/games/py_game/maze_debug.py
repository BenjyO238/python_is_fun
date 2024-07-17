import pygame

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Movement Test")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Player properties
player_size = 50
player_x = WIDTH // 2
player_y = HEIGHT // 2
player_speed = 5

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Clear the screen
    screen.fill(WHITE)

    # Draw player
    pygame.draw.rect(screen, RED, (player_x, player_y, player_size, player_size))

    # Update the display
    pygame.display.flip()

    # Control the game speed
    clock.tick(60)

pygame.quit()