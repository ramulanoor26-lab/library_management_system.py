# library_management_system.py

class Book:
    def __init__(self, book_id, title, author, available=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = available

    def to_string(self):
        return f"{self.book_id},{self.title},{self.author},{self.available}"

    @staticmethod
    def from_string(data):
        book_id, title, author, available = data.strip().split(",")
        return Book(book_id, title, author, available == "True")


class Library:
    def __init__(self, filename="books.txt"):
        self.filename = filename
        self.books = []
        self.load_books()

    def load_books(self):
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    self.books.append(Book.from_string(line))
        except FileNotFoundError:
            pass

    def save_books(self):
        with open(self.filename, "w") as file:
            for book in self.books:
                file.write(book.to_string() + "\n")

    def add_book(self):
        book_id = input("Book ID: ")
        title = input("Title: ")
        author = input("Author: ")
        self.books.append(Book(book_id, title, author))
        self.save_books()
        print("Book added successfully.")

    def view_books(self):
        for book in self.books:
            status = "Available" if book.available else "Borrowed"
            print(f"{book.book_id} | {book.title} | {book.author} | {status}")

    def borrow_book(self):
        book_id = input("Enter Book ID: ")
        for book in self.books:
            if book.book_id == book_id and book.available:
                book.available = False
                self.save_books()
                print("Book borrowed.")
                return
        print("Book not available.")

    def return_book(self):
        book_id = input("Enter Book ID: ")
        for book in self.books:
            if book.book_id == book_id and not book.available:
                book.available = True
                self.save_books()
                print("Book returned.")
                return
        print("Invalid return request.")

    def menu(self):
        while True:
            print("\n--- Library Management System ---")
            print("1. Add Book")
            print("2. View Books")
            print("3. Borrow Book")
            print("4. Return Book")
            print("5. Exit")

            choice = input("Choose option: ")

            if choice == "1":
                self.add_book()
            elif choice == "2":
                self.view_books()
            elif choice == "3":
                self.borrow_book()
            elif choice == "4":
                self.return_book()
            elif choice == "5":
                break
            else:
                print("Invalid option.")


if __name__ == "__main__":
    Library().menu()
