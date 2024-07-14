
## Favorite Colors

def favorite_colors(colors):
    """Print each color in the list."""
    for color in colors:
        print(color)

# Example invocation
my_colors = ["blue", "red", "green", "purple"]
favorite_colors(my_colors)



## Fruit Counter

def count_fruits(fruits):
    """Count the number of fruits in the list."""
    return len(fruits)

# Example invocation
fruit_basket = ["apple", "banana", "orange", "pear", "grape"]
print(f"Number of fruits: {count_fruits(fruit_basket)}")



## Name Reverser

def reverse_name(name):
    """Reverse the letters in a name."""
    return name[::-1]

# Example invocation
original_name = "Alice"
reversed_name = reverse_name(original_name)
print(f"{original_name} reversed is {reversed_name}")



## Grade Average

def calculate_average(grades):
    """Calculate the average of a list of grades."""
    return sum(grades) / len(grades)

# Example invocation
math_grades = [85, 90, 88, 92, 95]
average = calculate_average(math_grades)
print(f"The average grade is: {average:.2f}")



# Team Roster

def create_team(names):
    """Create a numbered team roster."""
    roster = {}
    for i, name in enumerate(names, 1):
        roster[i] = name
    return roster

# Example invocation
players = ["John", "Emma", "Alex", "Sophia"]
team_roster = create_team(players)
print("Team Roster:")
for number, name in team_roster.items():
    print(f"{number}: {name}")



## Word Length Counter

def word_lengths(sentence):
    """Count the length of each word in a sentence."""
    words = sentence.split()
    return [len(word) for word in words]

# Example invocation
my_sentence = "The quick brown fox jumps over the lazy dog"
lengths = word_lengths(my_sentence)
print(f"Word lengths: {lengths}")



## Unique Numbers

def unique_numbers(numbers):
    """Return a list of unique numbers."""
    return list(set(numbers))

# Example invocation
number_list = [1, 2, 2, 3, 4, 4, 5, 5, 6]
unique = unique_numbers(number_list)
print(f"Unique numbers: {unique}")

## Subject Grade Tracker

def track_grades(subjects_grades):
    """Track grades for different subjects."""
    for subject, grade in subjects_grades.items():
        print(f"{subject}: {grade}")

# Example invocation
grades = {"Math": 90, "Science": 85, "English": 88, "History": 92}
track_grades(grades)




## Friend Birthday Dictionary

def add_birthday(birthdays, name, date):
    """Add a friend's birthday to the dictionary."""
    birthdays[name] = date
    return birthdays

# Example invocation
friend_birthdays = {"Alice": "March 15", "Bob": "July 4"}
updated_birthdays = add_birthday(friend_birthdays, "Charlie", "December 25")
print("Updated birthday list:")
for friend, birthday in updated_birthdays.items():
    print(f"{friend}: {birthday}")



## Song Playlist

def create_playlist(songs):
    """Create a numbered playlist from a list of songs."""
    return list(enumerate(songs, 1))

# Example invocation
my_songs = ["Shape of You", "Blinding Lights", "Dance Monkey", "Uptown Funk"]
playlist = create_playlist(my_songs)
print("My Playlist:")
for number, song in playlist:
    print(f"{number}. {song}")




## More Elaborate emperature Converter

def convert_temperatures(temps, to_fahrenheit=True):
    """Convert a list of temperatures between Celsius and Fahrenheit."""
    if to_fahrenheit:
        return [temp * 9/ 5 + 32 for temp in temps]
    else:
        return [(temp - 32) * 5 / 9 for temp in temps]


# Example invocation
celsius_temps = [0, 10, 20, 30, 40]
fahrenheit_temps = convert_temperatures(celsius_temps)
print(f"Celsius: {celsius_temps}")
print(f"Fahrenheit: {fahrenheit_temps}")


## Movie Rating Analyzer

def analyze_ratings(ratings):
    """Analyze a dictionary of movie ratings."""
    return {
        "highest": max(ratings, key=ratings.get),
        "lowest": min(ratings, key=ratings.get),
        "average": sum(ratings.values()) / len(ratings)
    }


# Example invocation
movie_ratings = {"The Matrix": 9, "Inception": 8.5, "Interstellar": 8.7, "The Godfather": 9.2}
analysis = analyze_ratings(movie_ratings)
print(f"Highest rated: {analysis['highest']}")
print(f"Lowest rated: {analysis['lowest']}")
print(f"Average rating: {analysis['average']:.2f}")


## Shopping List Manager

def manage_shopping_list(shopping_list, item, action):
    """Add or remove items from a shopping list."""
    if action == "add":
        shopping_list.append(item)
    elif action == "remove" and item in shopping_list:
        shopping_list.remove(item)
    return shopping_list


# Example invocation
my_list = ["apples", "bread", "milk"]
my_list = manage_shopping_list(my_list, "eggs", "add")
print(f"After adding eggs: {my_list}")
my_list = manage_shopping_list(my_list, "bread", "remove")
print(f"After removing bread: {my_list}")


## Word Frequency Counter

def count_word_frequency(text):
    """Count the frequency of words in a text."""
    words = text.lower().split()
    return {word: words.count(word) for word in set(words)}


# Example invocation
sample_text = "The quick brown fox jumps over the lazy dog. The dog barks."
frequency = count_word_frequency(sample_text)
print("Word frequencies:")
for word, count in frequency.items():
    print(f"{word}: {count}")


## Team Score Tracker

def update_scores(scores, team, points):
    """Update team scores in a tournament."""
    if team in scores:
        scores[team] += points
    else:
        scores[team] = points
    return scores


# Example invocation
tournament_scores = {"Team A": 10, "Team B": 15}
tournament_scores = update_scores(tournament_scores, "Team A", 5)
tournament_scores = update_scores(tournament_scores, "Team C", 20)
print("Updated tournament scores:")
for team, score in tournament_scores.items():
    print(f"{team}: {score}")


## Subject Grade Averager

def average_subject_grades(grades):
    """Calculate average grades for each subject."""
    averages = {}
    for subject, grade_list in grades.items():
        averages[subject] = sum(grade_list) / len(grade_list)
    return averages


# Example invocation
student_grades = {
    "Math": [90, 85, 92],
    "Science": [88, 91, 87],
    "English": [85, 89, 92]
}
avg_grades = average_subject_grades(student_grades)
print("Average grades per subject:")
for subject, average in avg_grades.items():
    print(f"{subject}: {average:.2f}")


## Playlist Merger

def merge_playlists(playlist1, playlist2):
    """Merge two playlists, removing duplicates."""
    return list(set(playlist1 + playlist2))


# Example invocation
rock_playlist = ["Bohemian Rhapsody", "Stairway to Heaven", "Hotel California"]
pop_playlist = ["Shape of You", "Blinding Lights", "Hotel California"]
merged = merge_playlists(rock_playlist, pop_playlist)
print(f"Merged playlist: {merged}")


## Book Library Manager

def manage_library(library, action, book):
    """Manage a library of books with availability."""
    if action == "add":
        library[book] = "available"
    elif action == "borrow" and book in library:
        library[book] = "borrowed"
    elif action == "return" and book in library:
        library[book] = "available"
    return library


# Example invocation
my_library = {"The Hobbit": "available", "1984": "borrowed"}
my_library = manage_library(my_library, "add", "To Kill a Mockingbird")
my_library = manage_library(my_library, "borrow", "The Hobbit")
print("Library status:")
for book, status in my_library.items():
    print(f"{book}: {status}")


##Student Grade Reporter

def generate_grade_report(grades):
    """Generate a detailed grade report for a student."""
    total = sum(grades.values())
    average = total / len(grades)
    return {
        "subjects": list(grades.keys()),
        "highest": max(grades, key=grades.get),
        "lowest": min(grades, key=grades.get),
        "average": average,
        "total": total
    }


# Example invocation
student_grades = {"Math": 90, "Science": 85, "English": 88, "History": 92}
report = generate_grade_report(student_grades)
print("Grade Report:")
print(f"Subjects: {', '.join(report['subjects'])}")
print(f"Highest grade in: {report['highest']}")
print(f"Lowest grade in: {report['lowest']}")
print(f"Average grade: {report['average']:.2f}")
print(f"Total points: {report['total']}")


## Class Schedule Organizer

def organize_schedule(classes):
    """Organize a weekly class schedule."""
    schedule = {day: [] for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]}
    for class_name, (day, time) in classes.items():
        schedule[day].append((time, class_name))
    for day in schedule:
        schedule[day].sort()  # Sort classes by time
    return schedule


# Example invocation
my_classes = {
    "Math": ("Monday", "09:00"),
    "History": ("Tuesday", "10:30"),
    "Science": ("Monday", "11:00"),
    "English": ("Wednesday", "09:30"),
    "Art": ("Friday", "14:00")
}
organized_schedule = organize_schedule(my_classes)
print("Weekly Schedule:")
for day, classes in organized_schedule.items():
    print(f"{day}:")
    for time, class_name in classes:
        print(f"  {time} - {class_name}")


# Remember the temperature conversion formula: (C * 9/5) + 32. Here's a function that does it.
# Temperature conversion formula: (F - 32) * 5/9 = C. Here's a function that does it.
def temperature_converter(temperature, unit):
    if unit.lower() == 'c':
        # Convert Celsius to Fahrenheit
        converted = (temperature * 9/5) + 32
        return f"{temperature}°C is equal to {converted:.2f}°F"
    elif unit.lower() == 'f':
        # Convert Fahrenheit to Celsius
        converted = (temperature - 32) * 5/9
        return f"{temperature}°F is equal to {converted:.2f}°C"
    else:
        return "Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit."

# To run this let's get input from the user:
temp = float(input("Enter the temperature: "))
unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ")

# Convert and display the result
result = temperature_converter(temp, unit)
print(result)

# Optional: Add some example conversions
print("\nSome common temperature conversions:")
examples = [(0, 'C'), (32, 'F'), (100, 'C'), (98.6, 'F')]
for temp, unit in examples:
    print(temperature_converter(temp, unit))









# Now to show you what a "main" method is.  We can use this to test our functions.

# if __name__ == "__main__":
#     print("This code only runs when example.py is executed directly.")
#     some_function()
