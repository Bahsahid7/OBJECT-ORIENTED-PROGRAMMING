# Demo Script

# Student: [Your Name]

from operations import *

print("="*50)
print("LIBRARY SYSTEM DEMO")
print("="*50)

# Add books
print("\n1. ADDING BOOKS")
add_book("111", "Python Basics", "John Smith", "Non-Fiction", 5)
add_book("222", "The Story", "Jane Doe", "Fiction", 3)
add_book("333", "Space Adventure", "Bob Lee", "Sci-Fi", 4)

print("\nTrying to add duplicate:")
add_book("111", "Another Book", "Someone", "Fiction", 2)

print("\nTrying invalid genre:")
add_book("555", "Bad Book", "Author", "Comedy", 3)

# Add members
print("\n\n2. ADDING MEMBERS")
add_member("M001", "Alice", "alice@email.com", "123 Main St")
add_member("M002", "Bob", "bob@email.com", "456 Oak St")
add_member("M003", "Charlie", "charlie@email.com", "789 Pine St")

print("\nTrying duplicate member:")
add_member("M001", "Duplicate", "dup@email.com", "999 Elm St")

# Search books
print("\n\n3. SEARCHING BOOKS")
print("Searching for 'Python':")
results = search_books("Python")
for book in results:
    print("  Found:", book["title"])

# Borrow books
print("\n\n4. BORROWING BOOKS")
borrow_book("M001", "111")
borrow_book("M001", "222")
borrow_book("M002", "333")

print("\nAlice tries to borrow 4th book:")
borrow_book("M001", "333")
borrow_book("M001", "222")  # already borrowed

# Show status
print("\n\n5. CURRENT STATUS")
show_all_books()
show_all_members()

# Return books
print("\n\n6. RETURNING BOOKS")
return_book("M001", "111")

print("\nCharlie tries to return book he didn't borrow:")
return_book("M003", "111")

# Update
print("\n\n7. UPDATING")
update_book("111", new_title="Advanced Python")
update_member("M001", new_email="alice.new@email.com")

# Delete
print("\n\n8. DELETING")
print("Try to delete book that's borrowed:")
delete_book("222")

return_book("M001", "222")
delete_book("222")

print("\nTry to delete member with borrowed books:")
delete_member("M002")

return_book("M002", "333")
delete_member("M002")

delete_member("M003")

# Final
print("\n\n9. FINAL STATUS")
show_all_books()
show_all_members()

print("\n" + "="*50)
print("DEMO DONE")
print("="*50)