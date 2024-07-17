import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Background')

# Load background image
background = pygame.image.load('background.png')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the screen with a color
    screen.fill((135, 206, 235))
    # Draw the background image
    screen.blit(background, (0, 0))

    pygame.display.flip()
