from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

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

@app.route('/')
def index():
    reset_game()
    return render_template('index.html', words=words, attempts=attempts, correctly_guessed_groups=correctly_guessed_groups)

@app.route('/select', methods=['POST'])
def select():
    selected_indices = request.json['selected_indices']
    check_word_selection(selected_indices)
    response = {
        'game_ended': game_ended,
        'game_end_message': game_end_message,
        'attempts': attempts,
        'words': words,
        'correctly_guessed_groups': correctly_guessed_groups
    }
    return jsonify(response)

@app.route('/reset', methods=['POST'])
def reset():
    reset_game()
    response = {
        'game_ended': game_ended,
        'game_end_message': game_end_message,
        'attempts': attempts,
        'words': words,
        'correctly_guessed_groups': correctly_guessed_groups
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
