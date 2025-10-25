# Tests
# Student: [Your Name]

from operations import *

print("="*50)
print("RUNNING TESTS")
print("="*50)

# Test 1
print("\nTest 1: Add book")
books.clear()
members.clear()
result = add_book("111", "Test Book", "Author", "Fiction", 5)
assert result == True
assert "111" in books
print("PASSED")

# Test 2
print("\nTest 2: No duplicate ISBN")
books.clear()
add_book("111", "Book One", "Author", "Fiction", 3)
result = add_book("111", "Book Two", "Author", "Fiction", 2)
assert result == False
print("PASSED")

# Test 3
print("\nTest 3: Invalid genre")
books.clear()
result = add_book("111", "Book", "Author", "BadGenre", 3)
assert result == False
print("PASSED")

# Test 4
print("\nTest 4: Cannot borrow when no copies")
books.clear()
members.clear()
add_book("111", "Book", "Author", "Fiction", 1)
add_member("M001", "Alice", "alice@email.com", "Address")
add_member("M002", "Bob", "bob@email.com", "Address")
borrow_book("M001", "111")
result = borrow_book("M002", "111")
assert result == False
print("PASSED")

# Test 5
print("\nTest 5: Max 3 books")
books.clear()
members.clear()
add_book("111", "Book 1", "Author", "Fiction", 5)
add_book("222", "Book 2", "Author", "Fiction", 5)
add_book("333", "Book 3", "Author", "Fiction", 5)
add_book("444", "Book 4", "Author", "Fiction", 5)
add_member("M001", "Alice", "alice@email.com", "Address")
borrow_book("M001", "111")
borrow_book("M001", "222")
borrow_book("M001", "333")
result = borrow_book("M001", "444")
assert result == False
print("PASSED")

# Test 6
print("\nTest 6: Cannot delete borrowed book")
books.clear()
members.clear()
add_book("111", "Book", "Author", "Fiction", 2)
add_member("M001", "Alice", "alice@email.com", "Address")
borrow_book("M001", "111")
result = delete_book("111")
assert result == False
print("PASSED")

# Test 7
print("\nTest 7: Cannot delete member with books")
books.clear()
members.clear()
add_book("111", "Book", "Author", "Fiction", 2)
add_member("M001", "Alice", "alice@email.com", "Address")
borrow_book("M001", "111")
result = delete_member("M001")
assert result == False
print("PASSED")

# Test 8
print("\nTest 8: Return book")
books.clear()
members.clear()
add_book("111", "Book", "Author", "Fiction", 2)
add_member("M001", "Alice", "alice@email.com", "Address")
borrow_book("M001", "111")
result = return_book("M001", "111")
assert result == True
print("PASSED")

# Test 9
print("\nTest 9: Search books")
books.clear()
add_book("111", "Python Book", "John", "Non-Fiction", 3)
add_book("222", "Java Book", "Jane", "Non-Fiction", 2)
results = search_books("Python")
assert len(results) == 1
print("PASSED")

# Test 10
print("\nTest 10: Update works")
books.clear()
members.clear()
add_book("111", "Old Title", "Author", "Fiction", 5)
add_member("M001", "Alice", "old@email.com", "Address")
update_book("111", new_title="New Title")
update_member("M001", new_email="new@email.com")
assert books["111"]["title"] == "New Title"
print("PASSED")

print("\n" + "="*50)
print("ALL TESTS PASSED!")
print("="*50)