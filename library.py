# Library records (book name : number of times borrowed)
library = {
    "Book1": 4,
    "Book2": 2,
    "Book3": 0,
    "Book4": 7,
    "Book5": 2
}

# 1. Average number of books borrowed
average = sum(library.values()) / len(library)
print("Average books borrowed:", average)

# 2. Book with highest and lowest borrowings
highest_book = max(library, key=library.get)
lowest_book = min(library, key=library.get)
print("Highest borrowed book:", highest_book)
print("Lowest borrowed book:", lowest_book)

# 3. Count books that are not borrowed (borrow count = 0)
not_borrowed = sum(1 for x in library.values() if x == 0)
print("Books not borrowed:", not_borrowed)

# 4. Most frequent borrow count (mode)
from collections import Counter
borrow_counts = list(library.values())
mode = Counter(borrow_counts).most_common(1)[0][0]
print("Most frequent borrow count (mode):", mode)
