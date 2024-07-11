import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Catch the Falling Objects")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Basket
basket_width, basket_height = 100, 20
basket_x = width // 2 - basket_width // 2
basket_y = height - basket_height - 10
basket_speed = 10

# Apple
apple_width, apple_height = 30, 30
apple_x = random.randint(0, width - apple_width)
apple_y = -apple_height
apple_speed = 5

# Score
score = 0
font = pygame.font.Font(None, 36)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and basket_x > 0:
        basket_x -= basket_speed
    if keys[pygame.K_RIGHT] and basket_x < width - basket_width:
        basket_x += basket_speed

    # Move the apple
    apple_y += apple_speed

    # Check for collision
    if (basket_y < apple_y + apple_height
            and basket_y + basket_height > apple_y
            and basket_x < apple_x + apple_width
            and basket_x + basket_width > apple_x):
        score += 1
        apple_x = random.randint(0, width - apple_width)
        apple_y = -apple_height

    # Reset apple if it goes off screen
    if apple_y > height:
        apple_x = random.randint(0, width - apple_width)
        apple_y = -apple_height

    # Fill the screen with white
    screen.fill(white)

    # Draw the basket
    pygame.draw.rect(screen, black,
                     (basket_x, basket_y, basket_width, basket_height))

    # Draw the apple
    pygame.draw.rect(screen, red,
                     (apple_x, apple_y, apple_width, apple_height))

    # Draw the score
    score_text = font.render(f"Score: {score}", True, black)
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(30)

# Quit Pygame
pygame.quit()
