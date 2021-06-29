with open("books.txt") as new_file:
    for book in new_file:
        book = book.strip()
        print(book)
