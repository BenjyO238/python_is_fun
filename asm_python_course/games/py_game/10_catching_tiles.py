import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Falling Tiles Game')

# Font for displaying score
font = pygame.font.Font(None, 36)
score = 0

# Define the colors and their speeds
colors = {
    (255, 0, 0): 3,  # Red tiles fall at speed 3
    (0, 255, 0): 5,  # Green tiles fall at speed 5
    (0, 0, 255): 7,  # Blue tiles fall at speed 7
}

# Define the Tile class
class Tile(pygame.sprite.Sprite):
    def __init__(self, color, speed):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 380)
        self.rect.y = -20  # Start above the screen
        self.speed = speed

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > 400:
            self.kill()  # Remove the tile if it falls off the screen

# Define the Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((100, 20))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.centerx = 200
        self.rect.bottom = 390

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT] and self.rect.right < 400:
            self.rect.x += 5

# Create instances of Player and Tile
player = Player()
sprites = pygame.sprite.Group(player)
tiles = pygame.sprite.Group()

# Set up the clock for a consistent frame rate
clock = pygame.time.Clock()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Add new tiles at random intervals
    if random.randint(1, 20) == 1:
        color, speed = random.choice(list(colors.items()))
        tile = Tile(color, speed)
        tiles.add(tile)
        sprites.add(tile)

    # Update the sprites
    sprites.update()

    # Check for collisions and update score
    for tile in tiles:
        if player.rect.colliderect(tile.rect):
            score += 1
            tile.kill()

    # Fill the screen with white
    screen.fill((255, 255, 255))
    # Draw the sprites on the screen
    sprites.draw(screen)

    # Render and display the score
    score_text = font.render(f'Score: {score}', True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()
    # Control the frame rate to 30 FPS
    clock.tick(30)
