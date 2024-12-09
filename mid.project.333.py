class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def about(self):
        print(f"{self.title} was written by {self.author} in {self.year}")

class BookKeeper(Book):
    def __init__(self, title, author, year, rating):
        super().__init__(title, author, year)
        self.rating = rating

    def about(self):
        super().about()
        print(f"{self.title} was written by {self.author} in {self.year} and it's rating is {self.rating}")

class BookManager(Book):
    def __init__(self):
        self.books = []

    def add_book(self, title, author, year):
        new_book = Book(title, author, year)
        self.books.append(new_book)
        print(f"Added: {title} by {author}, {year}")

    def list_books(self):
        if not self.books:
            print("No books in the list.")
        else:
            print("Books in the list:")
            for index, book in enumerate(self.books, start=1):
                print(f"{index}. {book.title} by {book.author}, {book.year}")

    def search_book(self, search_term):
        found_books = [book for book in self.books if search_term.lower() in book.title.lower()]
        if not found_books:
            print(f"No books found with '{search_term}' in the title.")
        else:
            print(f"Books found with '{search_term}':")
            for book in found_books:
                book.about()


mark = Book("Uncle", "Mark", 1990)
mark.about()

george = BookKeeper("george", "john", 1990, 8)
george.about()

# Example usage
manager = BookManager()

# Adding books
manager.add_book("Uncle Tom's Cabin", "Harriet Beecher Stowe", 1852)
manager.add_book("Moby Dick", "Herman Melville", 1851)
manager.add_book("1984", "George Orwell", 1949)

# Listing all books
manager.list_books()

# Searching for a book
manager.search_book("1984")
manager.search_book("Tom")
manager.search_book("Harry")