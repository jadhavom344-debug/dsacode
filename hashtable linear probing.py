class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    # Hash Function (Division Method)
    def hash_fun(self, key):
        return key % self.size

    # Insert Key
    def insert(self, key):
        index = self.hash_fun(key)

        # Linear Probing
        for i in range(self.size):
            new_index = (index + i) % self.size
            if self.table[new_index] is None or self.table[new_index] == "DELETED":
                self.table[new_index] = key
                print(f" Key {key} inserted at index {new_index}")
                return

        print("Hash Table is Full! Cannot Insert.")

    # Search Key
    def search(self, key):
        index = self.hash_fun(key)

        for i in range(self.size):
            new_index = (index + i) % self.size
            if self.table[new_index] is None:
                print(" Key Not Found!")
                return
            if self.table[new_index] == key:
                print(f" Key {key} found at index {new_index}")
                return
        print(" Key Not Found!")

    # Delete Key
    def delete(self, key):
        index = self.hash_fun(key)

        for i in range(self.size):
            new_index = (index + i) % self.size
            if self.table[new_index] is None:
                print(" Key Not Found!")
                return
            if self.table[new_index] == key:
                self.table[new_index] = "DELETED"
                print(f"️ Key {key} deleted from index {new_index}")
                return
        print(" Key Not Found!")

    # Display Hash Table
    def display(self):
        print("\n Current Hash Table:")
        for i in range(self.size):
            print(f"Index {i}: {self.table[i]}")
        print()


# -------------------------------
# Main Program
# -------------------------------
size = int(input("Enter size of Hash Table: "))
ht = HashTable(size)

while True:
    print("\n1. Insert Key")
    print("2. Search Key")
    print("3. Delete Key")
    print("4. Display Table")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        key = int(input("Enter key to insert: "))
        ht.insert(key)

    elif choice == 2:
        key = int(input("Enter key to search: "))
        ht.search(key)

    elif choice == 3:
        key = int(input("Enter key to delete: "))
        ht.delete(key)

    elif choice == 4:
        ht.display()

    elif choice == 5:
        print(" Exiting Program...")
        break

    else:
        print("Invalid Choice! Try again.")

