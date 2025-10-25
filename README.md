# Library Management System

Student: Alhassan S B Sesay
Student ID:905005452
Course: PROG211 - Object-Oriented Programming 1  
Assignment: Mini Library Management System  

## What This Project Does

This is a simple library management system made with Python. It helps manage books, library members, and borrowing/returning books.

## Files in This Project

- `operations.py` - Main file with all functions
- `demo.py` - Shows how the system works
- `tests.py` - Tests to check if everything works
- `README.md` - This file
- `DesignRationale.pdf` - Explains why I used dictionary, list, and tuple
- `UML_Diagram.pdf` - Hand-drawn diagram showing the system

## Data Structures Used
I used dictionary because it's fast to find books using ISBN.


### 2. List (for Members)
I used list to keep all members in order.


### 3. Tuple (for Valid Genres)
I used tuple because genres should not change.

## How to Run

## Run the Demo
demo.py
This will show all features of the system.


### Run the Tests
python tests.py
This will test if everything works correctly.


## Main Functions

### Book Functions
- `add_book()` - Add a new book
- `search_books()` - Find books by title or author
- `update_book()` - Change book information
- `delete_book()` - Remove a book
- `show_all_books()` - Display all books

### Member Functions
- `add_member()` - Add a new member
- `update_member()` - Change member information
- `delete_member()` - Remove a member
- `show_all_members()` - Display all members

### Borrow/Return Functions
- `borrow_book()` - Member borrows a book
- `return_book()` - Member returns a book

## Rules

- Each book has a unique ISBN
- Each member has a unique ID
- Members can borrow maximum 3 books
- Cannot delete books if someone borrowed them
- Cannot delete members if they have borrowed books
- Only valid genres are allowed

## Tests Included

1. Add book successfully
2. Prevent duplicate ISBN
3. Reject invalid genre
4. Cannot borrow when no copies available
5. Maximum 3 books per member
6. Cannot delete book with borrowed copies
7. Cannot delete member with borrowed books
8. Return book successfully
9. Search books works correctly
10. Update book and member works

## What I Learned

- How to use dictionaries for fast lookup
- How to use lists to store multiple items
- How to use tuples for fixed data
- How to create functions in Python
- How to test my code using assert
- How to handle errors