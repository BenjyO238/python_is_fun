import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
DICE_SIZE = 100
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Load dice images
dice_images = [pygame.image.load(f'dice{i}.png') for i in range(1, 7)]


# Dice class
class Dice:
    def __init__(self):
        self.value = random.randint(1, 6)

    def roll(self):
        self.value = random.randint(1, 6)

    def draw(self, screen, x, y):
        screen.blit(dice_images[self.value - 1], (x, y))


# Game class
class CrapsGame:
    def __init__(self, player_name):
        self.player_name = player_name
        self.balance = 100
        self.current_bet = 0
        self.dice1 = Dice()
        self.dice2 = Dice()
        self.point = None
        self.game_over = False

    def place_bet(self, amount):
        if amount <= self.balance:
            self.current_bet = amount
            self.balance -= amount
        else:
            self.current_bet = 0

    def roll_dice(self):
        self.dice1.roll()
        self.dice2.roll()
        return self.dice1.value + self.dice2.value

    def check_roll(self, roll):
        if self.point is None:
            if roll in (7, 11):
                self.balance += self.current_bet * 2
                return "Win"
            elif roll in (2, 3, 12):
                return "Lose"
            else:
                self.point = roll
                return "Point"
        else:
            if roll == self.point:
                self.balance += self.current_bet * 2
                return "Win"
            elif roll == 7:
                return "Lose"
            else:
                return "Roll Again"

    def reset(self):
        self.point = None
        self.current_bet = 0
        self.game_over = False


def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Craps Game")

    font = pygame.font.Font(None, 36)
    small_font = pygame.font.Font(None, 28)

    # Start the game
    player_name = input("Enter your name: ")
    game = CrapsGame(player_name)

    clock = pygame.time.Clock()
    rolling = False
    result_text = ""

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not rolling:
                    if game.current_bet > 0 or game.point:
                        rolling = True
                        roll = game.roll_dice()
                        result = game.check_roll(roll)
                        if result in ("Win", "Lose"):
                            result_text = result
                            game.game_over = True
                        rolling = False
                elif event.key == pygame.K_RETURN and not rolling:
                    if game.game_over:
                        game.reset()
                        result_text = ""
                    else:
                        bet = int(input("Place your bet: "))
                        game.place_bet(bet)

        screen.fill(WHITE)
        game.dice1.draw(screen, SCREEN_WIDTH // 2 - DICE_SIZE, SCREEN_HEIGHT // 2 - DICE_SIZE // 2)
        game.dice2.draw(screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - DICE_SIZE // 2)

        balance_text = font.render(f"Balance: ${game.balance}", True, BLACK)
        screen.blit(balance_text, (50, 50))

        bet_text = font.render(f"Current Bet: ${game.current_bet}", True, BLACK)
        screen.blit(bet_text, (50, 100))

        result_text_surface = font.render(result_text, True, RED)
        screen.blit(result_text_surface,
                    (SCREEN_WIDTH // 2 - result_text_surface.get_width() // 2, SCREEN_HEIGHT - 100))

        if game.point:
            point_text = small_font.render(f"Point to Hit: {game.point}", True, BLACK)
            screen.blit(point_text, (SCREEN_WIDTH // 2 - point_text.get_width() // 2, SCREEN_HEIGHT // 2 + DICE_SIZE))

        pygame.display.flip()
        clock.tick(30)


if __name__ == "__main__":
    main()
