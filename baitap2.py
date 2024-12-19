class Book(object) :
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def book_storage(self):
        return(f"The book {self.title}, by {self.author}, in {self.year}")

class Library(object):
    def __init__(self):
        self.books = [ ]

    def add_book(self, title, author, year):
        book = Book(title = title, author = author, year = year)
        self.books.append(book)

    def search_by_author(self, author):
        titles = [ ]
        for book in self.books :
            if book.author == author :
                titles.append(book.title)
        return titles

    def list_books(self) :
        if not self.books :
            print("No book in the library")
        else:
            for book in self.books :
                print(book.book_storage())

if __name__ == '__main__':
    library = Library()


    library.add_book(title="Hello Earth", author="Orwell", year=1949)
    library.add_book(title="Hello Mommy", author="Orwell", year=1950)
    library.add_book(title="Hello World", author="Lee", year=1960)


    library.list_books()

    print("\nBooks by Orwell:")
    print(library.search_by_author(author="Orwell"))