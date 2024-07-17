import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Scoring System')

# Font for displaying score
font = pygame.font.Font(None, 36)
score = 0
collision_occurred = False

# Define the Ball class
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (0, 0, 255), (10, 10), 10)
        self.rect = self.image.get_rect()
        self.rect.center = (300, 200)  # Start the ball away from the player
        self.speed_x = 3
        self.speed_y = 3

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.left <= 0 or self.rect.right >= 400:
            self.speed_x = -self.speed_x
        if self.rect.top <= 0 or self.rect.bottom >= 400:
            self.speed_y = -self.speed_y

# Define the Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (0, 255, 0), (25, 25), 25)
        self.rect = self.image.get_rect()
        self.rect.center = (100, 200)  # Start the player away from the ball

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

# Create instances of Player and Ball
player = Player()
ball = Ball()
sprites = pygame.sprite.Group(player, ball)

# Set up the clock for a consistent frame rate
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update the sprites
    sprites.update()

    # Check for collision and update score
    if player.rect.colliderect(ball.rect):
        if not collision_occurred:
            score += 1
            collision_occurred = True
    else:
        collision_occurred = False

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
