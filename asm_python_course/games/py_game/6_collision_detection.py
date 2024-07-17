import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Collision Detection')

x, y = 200, 200
speed = 5

# Center the target square in the middle of the screen
'''
pygame.Rect(left, top, width, height)
left: The x-coordinate of the top-left corner of the rectangle.
top: The y-coordinate of the top-left corner of the rectangle.
width: The width of the rectangle.
height: The height of the rectangle.
'''
target_size = 50
target = pygame.Rect(
    (screen.get_width() // 2) - (target_size // 2),
    (screen.get_height() // 2) - (target_size // 2),
    target_size,
    target_size
)

# Clock to control the frame rate
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    player = pygame.Rect(x - 20, y - 20, 40, 40)

    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (255, 0, 0), target)
    pygame.draw.circle(screen, (0, 0, 255), (x, y), 20)

    if player.colliderect(target):
        font = pygame.font.Font(None, 36)
        text = font.render('Collision!', True, (0, 255, 0))
        screen.blit(text, (150, 180))

    pygame.display.flip()
    clock.tick(30)  # Control the frame rate to 30 FPS
