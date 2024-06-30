import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FONT_SIZE = 30

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GRAY = (200, 200, 200)
LIGHT_GRAY = (240, 240, 240)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("NYT Connections Game")
font = pygame.font.Font(None, FONT_SIZE)

# Game variables
words = [
    "PERSONAL", "PORT", "MAJOR", "OUTLET",
    "PRIVATE", "DEMAND", "POP-UP", "MARKET",
    "AUDIENCE", "WANT", "CAPTAIN", "JACK",
    "GENERAL", "APPETITE", "SOCKET", "ATTACK"
]
correct_groups = [
    {"PORT", "OUTLET", "JACK", "SOCKET"},
    {"CAPTAIN", "MAJOR", "GENERAL", "PRIVATE"},
    {"APPETITE", "DEMAND", "WANT", "MARKET"},
    {"PERSONAL", "POP-UP", "AUDIENCE", "ATTACK"}
]
selected_indices = []
correctly_guessed_groups = []
attempts = 4
game_ended = False
game_end_message = ""


def shuffle_words():
    global words
    random.shuffle(words)


def reset_game():
    global words, selected_indices, correct_groups, attempts, correctly_guessed_groups, game_ended, game_end_message
    words = [
        "PERSONAL", "PORT", "MAJOR", "OUTLET",
        "PRIVATE", "DEMAND", "POP-UP", "MARKET",
        "AUDIENCE", "WANT", "CAPTAIN", "JACK",
        "GENERAL", "APPETITE", "SOCKET", "ATTACK"
    ]
    shuffle_words()
    selected_indices = []
    correct_groups = [
        {"PORT", "OUTLET", "JACK", "SOCKET"},
        {"CAPTAIN", "MAJOR", "GENERAL", "PRIVATE"},
        {"APPETITE", "DEMAND", "WANT", "MARKET"},
        {"PERSONAL", "POP-UP", "AUDIENCE", "ATTACK"}
    ]
    attempts = 4
    correctly_guessed_groups = []
    game_ended = False
    game_end_message = ""


def display_game():
    screen.fill(WHITE)
    y_offset = 50

    # Display correctly guessed groups
    for group in correctly_guessed_groups:
        text = font.render(", ".join(group), True, GREEN)
        screen.blit(text, (50, y_offset))
        y_offset += 40

    # Display word choices
    y_offset += 20
    for i, word in enumerate(words):
        x_offset = 50 + (i % 4) * 175
        y = y_offset + (i // 4) * 75
        color = LIGHT_GRAY if i not in selected_indices else GRAY
        pygame.draw.rect(screen, color, (x_offset, y, 160, 60))
        text = font.render(word, True, BLACK)
        text_rect = text.get_rect(center=(x_offset + 80, y + 30))
        screen.blit(text, text_rect)

    # Display attempts left
    attempts_text = font.render(f"Attempts left: {attempts}", True, BLACK)
    screen.blit(attempts_text, (50, y_offset + 300))

    # Display game end message
    if game_ended:
        end_message_text = font.render(game_end_message, True, RED if "lose" in game_end_message else GREEN)
        screen.blit(end_message_text, (50, y_offset + 350))

    # Display buttons
    pygame.draw.rect(screen, YELLOW, (50, y_offset + 400, 150, 50))
    play_again_text = font.render("Play Again", True, BLACK)
    screen.blit(play_again_text, (60, y_offset + 415))

    pygame.draw.rect(screen, RED, (250, y_offset + 400, 150, 50))
    quit_text = font.render("Quit", True, BLACK)
    screen.blit(quit_text, (300, y_offset + 415))

    pygame.display.flip()


def check_word_selection(selected_indices):
    global selected_words, correctly_guessed_groups, correct_groups, words, attempts, game_ended, game_end_message
    selected_words = [words[i] for i in selected_indices]

    # Check if the selected words form a correct group
    if set(selected_words) in correct_groups:
        correctly_guessed_groups.append(selected_words.copy())
        correct_groups.remove(set(selected_words))
        words = [word for word in words if word not in selected_words]
        selected_words = []
        if not correct_groups:
            game_end_message = "Congratulations, you won!"
            game_ended = True
    else:
        attempts -= 1
        selected_words = []
        if attempts == 0:
            game_end_message = "Sorry, you lose!"
            game_ended = True


def main():
    global selected_indices
    reset_game()
    running = True
    selected_indices = []

    while running:
        display_game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.VIDEORESIZE:
                global SCREEN_WIDTH, SCREEN_HEIGHT
                SCREEN_WIDTH, SCREEN_HEIGHT = event.w, event.h
                screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if 50 <= mouse_pos[0] <= 200 and (SCREEN_HEIGHT - 150) <= mouse_pos[1] <= (SCREEN_HEIGHT - 100):
                    reset_game()
                elif 250 <= mouse_pos[0] <= 400 and (SCREEN_HEIGHT - 150) <= mouse_pos[1] <= (SCREEN_HEIGHT - 100):
                    running = False

                for i, word in enumerate(words):
                    x_offset = 50 + (i % 4) * 175
                    y_offset = 50 + (i // 4) * 75
                    if x_offset <= mouse_pos[0] <= x_offset + 160 and y_offset <= mouse_pos[1] <= y_offset + 60:
                        if i not in selected_indices:
                            selected_indices.append(i)
                        else:
                            selected_indices.remove(i)

                if len(selected_indices) == 4:
                    check_word_selection(selected_indices)
                    selected_indices = []

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
