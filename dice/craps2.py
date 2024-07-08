import pygame
import random
import time

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Craps Dice Game")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

font = pygame.font.Font(None, 36)

class Dice:
    def __init__(self):
        self.value = 1
        self.rolling = False
        self.roll_time = 0

    def roll(self):
        self.rolling = True
        self.roll_time = time.time()

    def update(self):
        if self.rolling:
            if time.time() - self.roll_time < 1:  # Roll for 1 second
                self.value = random.randint(1, 6)
            else:
                self.rolling = False

class CrapsGame:
    def __init__(self):
        self.dice1 = Dice()
        self.dice2 = Dice()
        self.point = 0
        self.bet = 0
        self.game_state = "NAME"
        self.player_name = ""
        self.balance = 100

    def place_bet(self, amount):
        if amount <= self.balance:
            self.bet = amount
            self.balance -= amount
            self.game_state = "FIRST_ROLL"
        else:
            print("Not enough balance")

    def roll_dice(self):
        self.dice1.roll()
        self.dice2.roll()

    def update(self):
        self.dice1.update()
        self.dice2.update()

        if not self.dice1.rolling and not self.dice2.rolling and self.game_state in ["FIRST_ROLL", "POINT_ROLL"]:
            total = self.dice1.value + self.dice2.value

            if self.game_state == "FIRST_ROLL":
                if total in [7, 11]:
                    self.game_state = "WIN"
                    self.balance += self.bet * 2
                elif total in [2, 3, 12]:
                    self.game_state = "LOSE"
                else:
                    self.point = total
                    self.game_state = "POINT_ROLL"
            elif self.game_state == "POINT_ROLL":
                if total == self.point:
                    self.game_state = "WIN"
                    self.balance += self.bet * 2
                elif total == 7:
                    self.game_state = "LOSE"

    def reset(self):
        self.point = 0
        self.bet = 0
        self.game_state = "BET"
        self.dice1.value = 1
        self.dice2.value = 1

def draw_text(text, x, y, color=WHITE):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

game = CrapsGame()

running = True
clock = pygame.time.Clock()
input_text = ""

def handle_name_input(event):
    global input_text
    if event.key == pygame.K_RETURN and input_text:
        game.player_name = input_text
        input_text = ""
        game.game_state = "BET"
    elif event.key == pygame.K_BACKSPACE:
        input_text = input_text[:-1]
    else:
        input_text += event.unicode

def handle_bet_input(event):
    global input_text
    if event.key == pygame.K_RETURN and input_text:
        try:
            bet_amount = int(input_text)
            if bet_amount <= game.balance:
                game.place_bet(bet_amount)
                input_text = ""
            else:
                print("Bet amount exceeds balance")
        except ValueError:
            print("Invalid bet amount")
    elif event.key == pygame.K_BACKSPACE:
        input_text = input_text[:-1]
    else:
        input_text += event.unicode

def handle_roll(event):
    if event.key == pygame.K_SPACE:
        game.roll_dice()

def handle_reset(event):
    if event.key == pygame.K_r:
        game.reset()

state_handlers = {
    "NAME": handle_name_input,
    "BET": handle_bet_input,
    "FIRST_ROLL": handle_roll,
    "POINT_ROLL": handle_roll,
    "WIN": handle_reset,
    "LOSE": handle_reset
}

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if game.game_state in state_handlers:
                state_handlers[game.game_state](event)

    game.update()

    screen.fill(BLACK)

    draw_text(f"Player: {game.player_name}", 10, 10)
    draw_text(f"Balance: ${game.balance}", 10, 50)
    draw_text(f"Bet: ${game.bet}", 10, 90)
    draw_text(f"Point: {game.point}", 10, 130)
    draw_text(f"Dice: {game.dice1.value} + {game.dice2.value} = {game.dice1.value + game.dice2.value}", 10, 170)

    state_messages = {
        "NAME": ["Enter your name and press ENTER:", input_text],
        "BET": ["Enter your bet and press ENTER:", "$" + input_text],
        "FIRST_ROLL": ["Press SPACE to roll dice", ""],
        "POINT_ROLL": ["Press SPACE to roll dice", ""],
        "WIN": ["You Win! Press R to play again", ""],
        "LOSE": ["You Lose! Press R to play again", ""]
    }

    message, value = state_messages[game.game_state]
    draw_text(message, WIDTH // 2 - 200, HEIGHT // 2 - 40)
    draw_text(value, WIDTH // 2 - 100, HEIGHT // 2)

    if game.game_state in ["WIN", "LOSE"]:
        color = GREEN if game.game_state == "WIN" else RED
        draw_text(message, WIDTH // 2 - 180, HEIGHT // 2, color)

    instructions = "ENTER: Confirm | SPACE: Roll | R: Reset"
    draw_text(instructions, WIDTH // 2 - 200, HEIGHT - 40, YELLOW)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()