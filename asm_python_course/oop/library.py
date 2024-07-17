# Define a class for a Book
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}"

# Define a class for a Library
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        return f"Added {book}"

    def list_books(self):
        return "Library books:\n" + "\n".join([str(book) for book in self.books])

# Create an instance of the Library class
library = Library()

# Get user input to add books
while True:
    title = input("Enter the book title (or 'quit' to stop): ")
    if title.lower() == 'quit':
        break
    author = input("Enter the book author: ")
    book = Book(title, author)
    print(library.add_book(book))

# List all books in the library
print(library.list_books())
