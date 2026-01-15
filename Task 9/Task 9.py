import os

FILE_NAME = "library_records.txt"

# Load books from file
def load_books():
    books = {}
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                book_id, title, author, status = line.strip().split(",")
                books[book_id] = {
                    "title": title,
                    "author": author,
                    "status": status
                }
    return books

# Save books to file
def save_books(books):
    with open(FILE_NAME, "w") as file:
        for book_id, details in books.items():
            file.write(f"{book_id},{details['title']},{details['author']},{details['status']}\n")

# Add book
def add_book(books):
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")

    books[book_id] = {
        "title": title,
        "author": author,
        "status": "Available"
    }
    save_books(books)
    print("Book added successfully")

# View books
def view_books(books):
    if not books:
        print("No books available.")
        return

    for book_id, details in books.items():
        print(f"{book_id} | {details['title']} | {details['author']} | {details['status']}")

# Issue book
def issue_book(books):
    book_id = input("Enter Book ID to issue: ")
    if book_id in books and books[book_id]["status"] == "Available":
        books[book_id]["status"] = "Issued"
        save_books(books)
        print("Book issued successfully")
    else:
        print("Book not available or invalid ID")

# Return book
def return_book(books):
    book_id = input("Enter Book ID to return: ")
    if book_id in books and books[book_id]["status"] == "Issued":
        books[book_id]["status"] = "Available"
        save_books(books)
        print("Book returned successfully")
    else:
        print("Invalid return request")

# Main Menu
def main():
    books = load_books()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. View Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book(books)
        elif choice == "2":
            view_books(books)
        elif choice == "3":
            issue_book(books)
        elif choice == "4":
            return_book(books)
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice")

# Run program
main()
