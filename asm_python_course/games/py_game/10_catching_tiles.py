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

# Define the colors, speeds, and scores
colors = {
    (255, 0, 0): (3, 1),  # Red tiles: speed 3, score 1
    (0, 255, 0): (5, 2),  # Green tiles: speed 5, score 2
    (0, 0, 255): (7, 5),  # Blue tiles: speed 7, score 5
}

# Define the Tile class
class Tile(pygame.sprite.Sprite):
    def __init__(self, color, speed, tile_score):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 380)
        self.rect.y = -20  # Start above the screen
        self.speed = speed
        self.tile_score = tile_score

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

    # Add new tiles at random intervals with adjusted probabilities
    if random.randint(1, 30) == 1:
        choice = random.choices(list(colors.items()), weights=[7, 5, 2])[0]
        color = choice[0]
        speed, tile_score = choice[1]
        tile = Tile(color, speed, tile_score)
        tiles.add(tile)
        sprites.add(tile)

    # Update the sprites
    sprites.update()

    # Check for collisions and update score
    for tile in tiles:
        if player.rect.colliderect(tile.rect):
            score += tile.tile_score
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
