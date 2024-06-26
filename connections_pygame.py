import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Connections Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GRAY = (200, 200, 200)

# Font
font = pygame.font.SysFont(None, 40)
small_font = pygame.font.SysFont(None, 30)

# Initialize game variables
words = [
    "Golf", "Ball", "Par", "Club",  # Golf terms
    "Hit", "Movie", "Song", "Run",  # "Hit" prefix
    "Cake", "Chocolate", "Candy", "Cookie",  # Sweets
    "Dog", "Cat", "Bird", "Fish"  # Pets
]
correct_groups = [
    {"Golf", "Ball", "Par", "Club"},
    {"Hit", "Movie", "Song", "Run"},
    {"Cake", "Chocolate", "Candy", "Cookie"},
    {"Dog", "Cat", "Bird", "Fish"}
]
selected_words = []
correctly_guessed_groups = []
attempts = 4
game_ended = False
game_end_message = ""


def shuffle_words():
    global words
    random.shuffle(words)


def reset_game():
    global words, selected_words, correct_groups, attempts, correctly_guessed_groups, game_ended, game_end_message
    words = [
        "Golf", "Ball", "Par", "Club",
        "Hit", "Movie", "Song", "Run",
        "Cake", "Chocolate", "Candy", "Cookie",
        "Dog", "Cat", "Bird", "Fish"
    ]
    shuffle_words()
    selected_words = []
    correct_groups = [
        {"Golf", "Ball", "Par", "Club"},
        {"Hit", "Movie", "Song", "Run"},
        {"Cake", "Chocolate", "Candy", "Cookie"},
        {"Dog", "Cat", "Bird", "Fish"}
    ]
    attempts = 4
    correctly_guessed_groups = []
    game_ended = False
    game_end_message = ""


def draw_button(text, color, x, y, width, height):
    pygame.draw.rect(screen, color, (x, y, width, height))
    text_surf = small_font.render(text, True, WHITE)
    text_rect = text_surf.get_rect(center=(x + width / 2, y + height / 2))
    screen.blit(text_surf, text_rect)
    return (x, y, width, height)


def game_over(message):
    screen.fill(WHITE)
    msg_text = font.render(message, True, RED if "lose" in message else GREEN)
    screen.blit(msg_text, (WIDTH / 2 - msg_text.get_width() / 2, HEIGHT / 2 - 100))
    play_again_btn = draw_button("Play Again", BLUE, WIDTH / 2 - 100, HEIGHT / 2, 200, 50)
    quit_btn = draw_button("Quit", BLUE, WIDTH / 2 - 100, HEIGHT / 2 + 60, 200, 50)
    pygame.display.flip()
    return play_again_btn, quit_btn


def display_game():
    screen.fill(WHITE)

    # Display correct guesses
    for j, group in enumerate(correctly_guessed_groups):
        for k, word in enumerate(group):
            word_text = font.render(word, True, GREEN)
            x = k * (WIDTH // 4) + 10
            y = j * 50 + 10
            pygame.draw.rect(screen, GREEN, (x, y, (WIDTH // 4) - 20, 40), 2)
            screen.blit(word_text, (x + 5, y + 5))

    # Display words
    word_start_y = HEIGHT // 3
    for i, word in enumerate(words):
        word_text = font.render(word, True, BLACK)
        x = (i % 4) * (WIDTH // 4) + 10
        y = (i // 4) * 70 + word_start_y
        color = YELLOW if word in selected_words else BLACK
        pygame.draw.rect(screen, color, (x, y, (WIDTH // 4) - 20, 60), 2)
        screen.blit(word_text, (x + 5, y + 10))

    # Display attempts
    attempts_text = font.render(f"Attempts left: {attempts}", True, RED)
    screen.blit(attempts_text, (10, HEIGHT - 60))

    pygame.display.flip()


def check_word_selection(mouse_x, mouse_y):
    global selected_words, correctly_guessed_groups, correct_groups, words, attempts, game_ended, game_end_message
    word_start_y = HEIGHT // 3
    for i, word in enumerate(words):
        x = (i % 4) * (WIDTH // 4) + 10
        y = (i // 4) * 70 + word_start_y
        if x < mouse_x < x + (WIDTH // 4) - 10 and y < mouse_y < y + 60:
            if word in selected_words:
                selected_words.remove(word)
            else:
                selected_words.append(word)

    # Check if the selected words form a correct group
    if len(selected_words) == 4:
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


def run():
    global game_ended

    reset_game()

    running = True
    while running:
        if not game_ended:
            display_game()
        else:
            play_again_btn, quit_btn = game_over(game_end_message)
            while game_ended:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        game_ended = False
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_x, mouse_y = event.pos
                        if play_again_btn[0] < mouse_x < play_again_btn[0] + play_again_btn[2] and play_again_btn[
                            1] < mouse_y < play_again_btn[1] + play_again_btn[3]:
                            reset_game()
                        elif quit_btn[0] < mouse_x < quit_btn[0] + quit_btn[2] and quit_btn[1] < mouse_y < quit_btn[1] + \
                                quit_btn[3]:
                            running = False
                            game_ended = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if not game_ended:
                    check_word_selection(mouse_x, mouse_y)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    run()
