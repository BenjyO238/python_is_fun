import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball Catch")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Ball properties
ball_radius = 20
ball_x = random.randint(ball_radius, WIDTH - ball_radius)
ball_y = ball_radius
ball_speed_x = 5
ball_speed_y = 5

# Paddle properties
paddle_width = 100
paddle_height = 20
paddle_x = WIDTH // 2 - paddle_width // 2
paddle_y = HEIGHT - paddle_height - 10

# Game variables
score = 0
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the paddle with mouse
    paddle_x = pygame.mouse.get_pos()[0] - paddle_width // 2

    # Update ball position
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Ball collision with walls
    if ball_x <= ball_radius or ball_x >= WIDTH - ball_radius:
        ball_speed_x = -ball_speed_x
    if ball_y <= ball_radius:
        ball_speed_y = -ball_speed_y

    # Ball collision with paddle
    if ball_y >= paddle_y - ball_radius and paddle_x < ball_x < paddle_x + paddle_width:
        ball_speed_y = -ball_speed_y
        score += 1

    # Ball out of bounds
    if ball_y > HEIGHT:
        ball_x = random.randint(ball_radius, WIDTH - ball_radius)
        ball_y = ball_radius

    # Clear the screen
    screen.fill(WHITE)

    # Draw the ball
    pygame.draw.circle(screen, RED, (int(ball_x), int(ball_y)), ball_radius)

    # Draw the paddle
    pygame.draw.rect(screen, BLUE, (paddle_x, paddle_y, paddle_width, paddle_height))

    # Display score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Control the game speed
    clock.tick(60)

pygame.quit()