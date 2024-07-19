import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Arrow properties
ARROW_WIDTH = 20
ARROW_HEIGHT = 20
ARROW_SPEED = 2  # Slower speed

# Shape positions
shape_positions = [
    (SCREEN_WIDTH - 160, 20, RED),
    (SCREEN_WIDTH - 120, 20, GREEN),
    (SCREEN_WIDTH - 80, 20, BLUE),
    (SCREEN_WIDTH - 40, 20, YELLOW)
]

# Arrow columns (aligned with shapes)
arrow_columns = [SCREEN_WIDTH - 160, SCREEN_WIDTH - 120, SCREEN_WIDTH - 80, SCREEN_WIDTH - 40]

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Friday Night Funkin Prototype")

# Arrow list
arrows = []

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Arrow generation timer
arrow_timer = 0
arrow_interval = 30  # Adjust this value to control the frequency of new arrows

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move arrows up
    for arrow in arrows:
        arrow[1] -= ARROW_SPEED

    # Add new arrow periodically in a random column
    arrow_timer += 1
    if arrow_timer >= arrow_interval:
        arrow_timer = 0
        column = random.choice(arrow_columns)
        new_arrow = [column, SCREEN_HEIGHT - 20]
        arrows.append(new_arrow)

    # Remove arrows that are off the screen
    arrows = [arrow for arrow in arrows if arrow[1] > -ARROW_HEIGHT]

    # Clear screen
    screen.fill(WHITE)

    # Draw shapes on the top
    for x, y, color in shape_positions:
        pygame.draw.rect(screen, color, (x, y, ARROW_WIDTH, ARROW_HEIGHT))

    # Draw arrows
    for arrow in arrows:
        pygame.draw.polygon(screen, RED, [
            (arrow[0], arrow[1]),
            (arrow[0] - ARROW_WIDTH // 2, arrow[1] + ARROW_HEIGHT),
            (arrow[0] + ARROW_WIDTH // 2, arrow[1] + ARROW_HEIGHT)
        ])

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(30)

# Quit Pygame
pygame.quit()
sys.exit()
