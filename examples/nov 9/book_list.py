FILE_NAME = "examples\nov 9\books.txt"



def load_books():
    books = []

    with open(FILE_NAME as file):
        for line in file:
            books.append(line.strip())
    return books



def display_books(Books):
    for book in books:
        print(F" - {book}")

def addbook(books):
    book =  input("Enter book name: ")
    books.append(book)
    print(f"{book} was successfully added. ")
    return books

def delete_book(books):
    userbook = input("Enter book name: ")

    for book in books:
        if userbook.lower().strip() == book.lower().strip():
            books.remove(book)
            print(f"{userbook} was successfully removed.")
    return load_books

print("Welcome to our book store")
books = load_books()


while True:
    command = input("(L)ist, (A)dd, (D)elete, (Q)uit: ").strip().lower()

    if command == "l":
        display_books(books)

    elif command == "a":
        books = add_books(books)

    elif command == "d":
        books = delete_books(books)

    elif command == "q":
        break

    else: print("Sorry, that's invalid input")

save_books(books)
print("Goodbye")