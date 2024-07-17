import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Adding Sprites')

# Define the Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (0, 0, 255), (25, 25), 25)
        self.rect = self.image.get_rect()
        self.rect.center = (200, 200)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5

# Create a player instance
player = Player()
# Create a group to hold the sprite(s)
sprites = pygame.sprite.Group(player)

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
    # Control the frame rate
    clock.tick(30)
