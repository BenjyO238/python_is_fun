import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Simple Animation')

# Define the Ball class
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (0, 0, 255), (10, 10), 10)
        self.rect = self.image.get_rect()
        self.rect.center = (200, 200)
        self.speed_x = 6
        self.speed_y = 6

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.left <= 0 or self.rect.right >= 400:
            self.speed_x = -self.speed_x
        if self.rect.top <= 0 or self.rect.bottom >= 400:
            self.speed_y = -self.speed_y

# Create a ball instance
ball = Ball()
# Create a group to hold the ball sprite
sprites = pygame.sprite.Group(ball)

# Set up the clock for a consistent frame rate
clock = pygame.time.Clock()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update the sprite(s)
    sprites.update()

    # Fill the screen with white
    screen.fill((255, 255, 255))
    # Draw the sprite(s) on the screen
    sprites.draw(screen)

    # Update the display
    pygame.display.flip()
    # Control the frame rate to 30 FPS
    clock.tick(30)
