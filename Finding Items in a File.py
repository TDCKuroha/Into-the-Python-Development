chosen_volume = input("Which volume of scripture would you like to learn about? ")

max_chapters = -1
book_with_max = ""

# Open the file with the information
with open("books_and_chapters.txt") as books_file:
    for line in books_file:
        parts = line.split(":")
        book = parts[0].strip()
        chapters = int(parts[1]) 
        testament = parts[2].strip()

        if testament.lower() == chosen_volume.lower():
            print(f"Scripture: {testament}, Book: {book}, Chapters: {chapters}")

            if chapters > max_chapters:
                max_chapters = chapters
                book_with_max = book

print(f"The book with the most chapters in the {chosen_volume} is: {book_with_max}")
print(f"It has {max_chapters} chapters.")
