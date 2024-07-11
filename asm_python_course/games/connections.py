import random

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


def display_game():
    print("\nCorrect Groups:")
    for group in correctly_guessed_groups:
        print(", ".join(group))

    print("\nWord Choices:")
    for i, word in enumerate(words):
        print(f"{i + 1}. {word}", end="  ")
        if (i + 1) % 4 == 0:
            print()
    print(f"\nAttempts left: {attempts}")


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


def run():
    reset_game()

    while not game_ended:
        display_game()

        try:
            selected_indices = input("Select 4 word indices separated by spaces: ").split()
            selected_indices = [int(index) - 1 for index in selected_indices]
            if len(selected_indices) == 4:
                check_word_selection(selected_indices)
            else:
                print("Please select exactly 4 words.")
        except ValueError:
            print("Invalid input. Please enter numbers only.")

    print(game_end_message)
    if game_end_message == "Congratulations, you won!":
        print("You correctly identified all groups!")
    else:
        print("Better luck next time.")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        run()
    else:
        print("Thanks for playing!")


if __name__ == "__main__":
    run()
