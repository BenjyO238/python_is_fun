import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders Clone")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Player properties
player_width = 50
player_height = 30
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - player_height - 10
player_speed = 5

# Alien properties
alien_width = 40
alien_height = 40
alien_speed = 1
aliens = []

# Bullet properties
bullet_width = 5
bullet_height = 15
bullet_speed = 7
bullets = []

# Game variables
score = 0
clock = pygame.time.Clock()

# Create aliens
for row in range(5):
    for col in range(10):
        alien_x = col * (alien_width + 10) + 50
        alien_y = row * (alien_height + 10) + 50
        aliens.append(pygame.Rect(alien_x, alien_y, alien_width, alien_height))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append(pygame.Rect(player_x + player_width // 2 - bullet_width // 2, player_y, bullet_width, bullet_height))

    # Move player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed

    # Move bullets
    for bullet in bullets[:]:
        bullet.y -= bullet_speed
        if bullet.y < 0:
            bullets.remove(bullet)

    # Move aliens
    for alien in aliens:
        alien.x += alien_speed
        if alien.left <= 0 or alien.right >= WIDTH:
            alien_speed = -alien_speed
            for a in aliens:
                a.y += 10

    # Check for collisions
    for bullet in bullets[:]:
        for alien in aliens[:]:
            if bullet.colliderect(alien):
                bullets.remove(bullet)
                aliens.remove(alien)
                score += 10
                break

    # Clear the screen
    screen.fill(WHITE)

    # Draw player
    pygame.draw.rect(screen, GREEN, (player_x, player_y, player_width, player_height))

    # Draw aliens
    for alien in aliens:
        pygame.draw.rect(screen, RED, alien)

    # Draw bullets
    for bullet in bullets:
        pygame.draw.rect(screen, GREEN, bullet)

    # Display score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Control the game speed
    clock.tick(60)

pygame.quit()