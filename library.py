
def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")

    with open("library.txt", "a") as file:
        file.write(title + "," + author + "\n")

    print("Book added successfully.")


def search_book():
    search = input("Enter title or author to search: ").lower()

    try:
        with open("library.txt", "r") as file:
            found = False

            for line in file:
                title, author = line.strip().split(",", 1)

                if search in title.lower() or search in author.lower():
                    print("Title:", title, "| Author:", author)
                    found = True

            if not found:
                print("Book not found.")

    except FileNotFoundError:
        print("Library catalogue is empty.")


def generate_report():
    try:
        with open("library.txt", "r") as file:
            books = [line.strip().split(",", 1)
                     for line in file if line.strip()]

        print("\nAll Books in Library:")
        for title, author in books:
            print("Title:", title, "| Author:", author)

        print("Total number of books:", len(books))

        author_name = input("Enter author name for report: ").lower()
        print("Books by", author_name + ":")

        found = False
        for title, author in books:
            if author.lower() == author_name:
                print(title)
                found = True

        if not found:
            print("No books found for this author.")

    except FileNotFoundError:
        print("Library catalogue is empty.")


while True:
    print("\n1. Add Book")
    print("2. Search Book")
    print("3. Generate Report")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        search_book()
    elif choice == "3":
        generate_report()
    elif choice == "4":
        print("Exiting program.")
        break
    else:
        print("Invalid choice.")
