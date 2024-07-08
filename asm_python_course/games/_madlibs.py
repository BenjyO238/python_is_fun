import random
import re

madlib_templates = {
    1: "The {adj1} {noun1} {verb1} over the {adj2} {noun2}. Suddenly, a {adj3} {noun3} {verb2} {adverb}, causing everyone to {verb3}.",
    2: "In a {adj1} {noun1}, scientists discovered a {adj2} {noun2} that could {verb1}. They decided to {verb2} it {adverb}, hoping to {verb3} the world's {noun3} problem.",
    3: "Captain {name} stood on the {adj1} deck of the {noun1}. With a {adj2} voice, they ordered the crew to {verb1} the {noun2}. As they sailed into the {adj3} sunset, everyone felt {adverb} {adj4}.",
    4: "The {adj1} chef {verb1} into the kitchen, ready to create a {adj2} dish. They mixed {noun1} with {noun2} and added a pinch of {adj3} {noun3}. The result was so {adj4} that it made the food critics {verb2} in delight.",
    5: "During the {adj1} {noun1} championship, the underdog team {verb1} their way to victory. Their {adj2} strategy involved using a secret {noun2} to {verb2} their opponents. In the end, they celebrated by {verb3} {adverb} around the {noun3}."
}


def get_user_input(prompt):
    while True:
        user_input = input(f"Enter {prompt}: ")
        if user_input.strip():
            return user_input
        else:
            print("Input cannot be empty. Please try again.")


def play_madlib(template_number):
    template = madlib_templates[template_number]
    words_needed = re.findall(r'\{(.*?)\}', template)  # Using regex to extract all placeholders

    print("\nYou will need to provide the following words:")
    for word in set(words_needed):
        print(word)

    user_inputs = {}
    for word in words_needed:
        if word.startswith('adj'):
            prompt = "an adjective"
        elif word.startswith('noun'):
            prompt = "a noun"
        elif word.startswith('verb'):
            prompt = "a verb"
        elif word == 'adverb':
            prompt = "an adverb"
        elif word == 'name':
            prompt = "a name"
        else:
            prompt = word

        user_inputs[word] = get_user_input(prompt)
        print(f"Collected {word}: {user_inputs[word]}")  # Debug print

    print(f"User inputs: {user_inputs}")  # Debug print

    try:
        completed_madlib = template.format(**user_inputs)
        print("\nYour completed Mad Lib:")
        print(completed_madlib)
    except KeyError as e:
        print(f"Error: Missing input for {e}")


def main():
    print("Welcome to the Mad Libs game!")
    print("Choose a template by number (1-5):")
    for i in range(1, 6):
        print(f"Template {i}")

    while True:
        try:
            template_number = int(input("Enter the template number: "))
            if 1 <= template_number <= 5:
                break
            else:
                print("Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")

    play_madlib(template_number)


if __name__ == "__main__":
    main()
