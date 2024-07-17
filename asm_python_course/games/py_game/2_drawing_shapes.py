import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Drawing Shapes')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))

    # Draw a rectangle
    pygame.draw.rect(screen, (255, 0, 0), (50, 50, 100, 100))
    # Draw a circle
    pygame.draw.circle(screen, (0, 255, 0), (200, 200), 50)

    pygame.display.flip()
