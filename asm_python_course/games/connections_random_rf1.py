import random
import yaml

class ConnectionsGame:
    def __init__(self, yaml_file):
        self.game_end_message = None
        self.game_ended = None
        self.attempts = None
        self.correctly_guessed_groups = None
        self.selected_words = None
        self.correct_groups = None
        self.words = None
        self.word_groups = None
        self.yaml_file = yaml_file
        self.load_word_groups()
        self.reset_game()

    def load_word_groups(self):
        with open(self.yaml_file, 'r') as file:
            self.word_groups = yaml.safe_load(file)['word_groups']

    def shuffle_words(self):
        random.shuffle(self.words)

    def pick_random_group(self):
        group = random.choice(self.word_groups)
        self.words = group['words']
        self.correct_groups = [set(group) for group in group['correct_groups']]

    def reset_game(self):
        self.pick_random_group()
        self.selected_words = []
        self.correctly_guessed_groups = []
        self.attempts = 4
        self.game_ended = False
        self.game_end_message = ""
        self.shuffle_words()

    def display_game(self):
        print("\nCorrect Groups:")
        for group in self.correctly_guessed_groups:
            print(", ".join(group))

        print("\nWord Choices:")
        for i, word in enumerate(self.words):
            print(f"{i + 1}. {word}", end="  ")
            if (i + 1) % 4 == 0:
                print()
        print(f"\nAttempts left: {self.attempts}")

    def check_word_selection(self, selected_indices):
        self.selected_words = [self.words[i] for i in selected_indices]

        # Check if the selected words form a correct group
        if set(self.selected_words) in self.correct_groups:
            self.correctly_guessed_groups.append(self.selected_words.copy())
            self.correct_groups.remove(set(self.selected_words))
            self.words = [word for word in self.words if word not in self.selected_words]
            self.selected_words = []
            if not self.correct_groups:
                self.game_end_message = "Congratulations, you won!"
                self.game_ended = True
        else:
            self.attempts -= 1
            self.selected_words = []
            if self.attempts == 0:
                self.game_end_message = "Sorry, you lose!"
                self.game_ended = True

    def run(self):
        self.reset_game()

        while not self.game_ended:
            self.display_game()

            try:
                selected_indices = input("Select 4 word indices separated by spaces: ").split()
                selected_indices = [int(index) - 1 for index in selected_indices]
                if len(selected_indices) == 4:
                    self.check_word_selection(selected_indices)
                else:
                    print("Please select exactly 4 words.")
            except ValueError:
                print("Invalid input. Please enter numbers only.")

        print(self.game_end_message)
        if self.game_end_message == "Congratulations, you won!":
            print("You correctly identified all groups!")
        else:
            print("Better luck next time.")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again == "yes":
            self.run()
        else:
            print("Thanks for playing!")


if __name__ == "__main__":
    game = ConnectionsGame("word_groups.yaml")
    game.run()
