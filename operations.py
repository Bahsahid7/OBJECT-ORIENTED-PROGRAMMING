# Library Management System
# Student: [Your Name]
# PROG211 - Assignment 1

# Data Structures
books = {}
members = []
VALID_GENRES = ("Fiction", "Non-Fiction", "Sci-Fi", "Mystery", "Romance", "History", "Biography", "Fantasy")


# Book Functions

def add_book(isbn, title, author, genre, copies):
    if isbn in books:
        print("Error: Book already exists!")
        return False

    if genre not in VALID_GENRES:
        print("Error: Invalid genre!")
        return False

    books[isbn] = {
        "title": title,
        "author": author,
        "genre": genre,
        "total_copies": copies,
        "available_copies": copies
    }
    print("Book added successfully!")
    return True


def search_books(keyword):
    results = []
    for isbn in books:
        if keyword.lower() in books[isbn]["title"].lower():
            results.append(books[isbn])
        elif keyword.lower() in books[isbn]["author"].lower():
            results.append(books[isbn])
    return results


def update_book(isbn, new_title=None, new_author=None):
    if isbn not in books:
        print("Error: Book not found!")
        return False

    if new_title:
        books[isbn]["title"] = new_title
    if new_author:
        books[isbn]["author"] = new_author

    print("Book updated!")
    return True


def delete_book(isbn):
    if isbn not in books:
        print("Error: Book not found!")
        return False

    if books[isbn]["available_copies"] < books[isbn]["total_copies"]:
        print("Error: Book is borrowed!")
        return False

    del books[isbn]
    print("Book deleted!")
    return True


# Member Functions

def add_member(member_id, name, email, address):
    for member in members:
        if member["member_id"] == member_id:
            print("Error: Member already exists!")
            return False

    members.append({
        "member_id": member_id,
        "name": name,
        "email": email,
        "address": address,
        "borrowed_books": []
    })
    print("Member added successfully!")
    return True


def update_member(member_id, new_name=None, new_email=None):
    for member in members:
        if member["member_id"] == member_id:
            if new_name:
                member["name"] = new_name
            if new_email:
                member["email"] = new_email
            print("Member updated!")
            return True

    print("Error: Member not found!")
    return False


def delete_member(member_id):
    for i in range(len(members)):
        if members[i]["member_id"] == member_id:
            if len(members[i]["borrowed_books"]) > 0:
                print("Error: Member has borrowed books!")
                return False
            members.pop(i)
            print("Member deleted!")
            return True

    print("Error: Member not found!")
    return False


# Borrow and Return Functions

def borrow_book(member_id, isbn):
    # Find member
    member = None
    for m in members:
        if m["member_id"] == member_id:
            member = m

    if member == None:
        print("Error: Member not found!")
        return False

    if isbn not in books:
        print("Error: Book not found!")
        return False

    if len(member["borrowed_books"]) >= 3:
        print("Error: Cannot borrow more than 3 books!")
        return False

    if books[isbn]["available_copies"] <= 0:
        print("Error: No copies available!")
        return False

    member["borrowed_books"].append(isbn)
    books[isbn]["available_copies"] = books[isbn]["available_copies"] - 1
    print("Book borrowed successfully!")
    return True


def return_book(member_id, isbn):
    # Find member
    member = None
    for m in members:
        if m["member_id"] == member_id:
            member = m

    if member == None:
        print("Error: Member not found!")
        return False

    if isbn not in member["borrowed_books"]:
        print("Error: Member did not borrow this book!")
        return False

    member["borrowed_books"].remove(isbn)
    books[isbn]["available_copies"] = books[isbn]["available_copies"] + 1
    print("Book returned successfully!")
    return True


# Display Functions

def show_all_books():
    print("\n--- ALL BOOKS ---")
    for isbn in books:
        print("ISBN:", isbn)
        print("Title:", books[isbn]["title"])
        print("Author:", books[isbn]["author"])
        print("Genre:", books[isbn]["genre"])
        print("Available:", books[isbn]["available_copies"], "/", books[isbn]["total_copies"])
        print("-" * 40)


def show_all_members():
    print("\n--- ALL MEMBERS ---")
    for member in members:
        print("ID:", member["member_id"])
        print("Name:", member["name"])
        print("Email:", member["email"])
        print("Borrowed Books:", len(member["borrowed_books"]))
        print("-" * 40)