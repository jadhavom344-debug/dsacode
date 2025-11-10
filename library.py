# Library records (book name : number of times borrowed)
# Library Borrowing Record Management System

# Sample data: book -> number of times borrowed
borrow_records = {
    "Harry Potter": 15,
    "The Hobbit": 7,
    "The Alchemist": 20,
    "C Programming": 0,
    "Data Structures": 12,
    "Maths Grade 12": 0,
    "Python Basics": 20
}

# 1. Compute Average
total = sum(borrow_records.values())
count = len(borrow_records)
average = total / count

# 2. Find Highest and Lowest Borrowed Books
highest_book = max(borrow_records, key=borrow_records.get)
lowest_book = min(borrow_records, key=borrow_records.get)

# 3. Count Books Not Borrowed (0 times)
not_borrowed_count = sum(1 for x in borrow_records.values() if x == 0)

# 4. Find Most Frequently Borrowed Book (Mode)
# If multiple books share same highest frequency, this picks the first
most_frequent_book = max(borrow_records, key=borrow_records.get)

# Display results
print("Average Borrow Count:", average)
print("Highest Borrowed Book:", highest_book, "->", borrow_records[highest_book])
print("Lowest Borrowed Book:", lowest_book, "->", borrow_records[lowest_book])
print("Number of Books Never Borrowed:", not_borrowed_count)
print("Most Frequently Borrowed Book:", most_frequent_book)

