import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Craps Dice Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Fonts
font = pygame.font.Font(None, 36)

class Dice:
    def __init__(self):
        self.value = 1

    def roll(self):
        self.value = random.randint(1, 6)

class CrapsGame:
    def __init__(self):
        self.dice1 = Dice()
        self.dice2 = Dice()
        self.point = 0
        self.bet = 0
        self.game_state = "BET"  # "BET", "FIRST_ROLL", "POINT_ROLL", "WIN", "LOSE"

    def place_bet(self, amount):
        self.bet = amount
        self.game_state = "FIRST_ROLL"

    def roll_dice(self):
        self.dice1.roll()
        self.dice2.roll()
        total = self.dice1.value + self.dice2.value

        if self.game_state == "FIRST_ROLL":
            if total in [7, 11]:
                self.game_state = "WIN"
            elif total in [2, 3, 12]:
                self.game_state = "LOSE"
            else:
                self.point = total
                self.game_state = "POINT_ROLL"
        elif self.game_state == "POINT_ROLL":
            if total == self.point:
                self.game_state = "WIN"
            elif total == 7:
                self.game_state = "LOSE"

    def reset(self):
        self.point = 0
        self.bet = 0
        self.game_state = "BET"

def draw_text(text, x, y, color=WHITE):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

game = CrapsGame()

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if game.game_state == "BET":
                if event.key == pygame.K_RETURN:
                    game.place_bet(10)  # Fixed bet of 10 for simplicity
            elif game.game_state in ["FIRST_ROLL", "POINT_ROLL"]:
                if event.key == pygame.K_SPACE:
                    game.roll_dice()
            elif game.game_state in ["WIN", "LOSE"]:
                if event.key == pygame.K_r:
                    game.reset()

    screen.fill(BLACK)

    draw_text(f"Bet: ${game.bet}", 10, 10)
    draw_text(f"Point: {game.point}", 10, 50)
    draw_text(f"Dice: {game.dice1.value} + {game.dice2.value} = {game.dice1.value + game.dice2.value}", 10, 90)

    if game.game_state == "BET":
        draw_text("Press ENTER to place bet", WIDTH // 2 - 150, HEIGHT // 2)
    elif game.game_state in ["FIRST_ROLL", "POINT_ROLL"]:
        draw_text("Press SPACE to roll dice", WIDTH // 2 - 150, HEIGHT // 2)
    elif game.game_state == "WIN":
        draw_text("You Win! Press R to play again", WIDTH // 2 - 180, HEIGHT // 2, GREEN)
    elif game.game_state == "LOSE":
        draw_text("You Lose! Press R to play again", WIDTH // 2 - 180, HEIGHT // 2, RED)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()