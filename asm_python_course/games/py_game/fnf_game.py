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

# Shape properties
SHAPE_WIDTH = 40
SHAPE_HEIGHT = 40
ENLARGED_SHAPE_SIZE = 60  # Enlarged size

# Shape positions (spread out horizontally)
shape_positions = [
    (SCREEN_WIDTH - 320, 20, RED),
    (SCREEN_WIDTH - 240, 20, GREEN),
    (SCREEN_WIDTH - 160, 20, BLUE),
    (SCREEN_WIDTH - 80, 20, YELLOW)
]

# Arrow columns (aligned with shapes)
arrow_columns = [
    SCREEN_WIDTH - 320 + SHAPE_WIDTH // 2,
    SCREEN_WIDTH - 240 + SHAPE_WIDTH // 2,
    SCREEN_WIDTH - 160 + SHAPE_WIDTH // 2,
    SCREEN_WIDTH - 80 + SHAPE_WIDTH // 2
]

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

# Key press state
key_press_state = [False, False, False, False]  # State for left, down, up, right keys
collision_detected = [False, False, False, False]  # State for collision detection

# Main game loop
running = True
while running:
    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                key_press_state[0] = True
            elif event.key == pygame.K_DOWN:
                key_press_state[1] = True
            elif event.key == pygame.K_UP:
                key_press_state[2] = True
            elif event.key == pygame.K_RIGHT:
                key_press_state[3] = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                key_press_state[0] = False
            elif event.key == pygame.K_DOWN:
                key_press_state[1] = False
            elif event.key == pygame.K_UP:
                key_press_state[2] = False
            elif event.key == pygame.K_RIGHT:
                key_press_state[3] = False

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
    for i, (x, y, color) in enumerate(shape_positions):
        enlarged = False
        # Check collision
        for arrow in arrows:
            if x <= arrow[0] - ARROW_WIDTH // 2 <= x + SHAPE_WIDTH and y <= arrow[1] <= y + SHAPE_HEIGHT:
                if key_press_state[i]:
                    enlarged = True
                    break

        size = ENLARGED_SHAPE_SIZE if enlarged else SHAPE_WIDTH
        shape_x = x - (size - SHAPE_WIDTH) // 2
        shape_y = y - (size - SHAPE_HEIGHT) // 2
        pygame.draw.rect(screen, color, (shape_x, shape_y, size, size))

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
