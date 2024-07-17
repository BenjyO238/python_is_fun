import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Displaying Text')

font = pygame.font.Font(None, 36)
text = font.render('Hello, Pygame!', True, (0, 0, 0))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))
    screen.blit(text, (50, 50))

    pygame.display.flip()
