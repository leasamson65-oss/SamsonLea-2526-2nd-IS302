class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display_book(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Year:", self.year)
        print()

# Create objects
book1_lea = Book("Python Programming", "John Smith", 2022)
book2_lea = Book("Data Structures", "Jane Doe", 2021)
book3_lea = Book("OOP Concepts", "Mark Lee", 2020)

# Display books
book1_lea.display_book()
book2_lea.display_book()
book3_lea.display_book()