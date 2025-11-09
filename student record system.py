# Student Record Management System using Singly Linked List

class Node:
    def _init_(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks
        self.next = None


class StudentList:
    def _init_(self):
        self.head = None

    # Add student (Insert at end)
    def add_student(self, roll, name, marks):
        new_node = Node(roll, name, marks)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # Display all students
    def display(self):
        if self.head is None:
            print("\nNo records found.\n")
            return

        print("\nStudent Records:")
        print("-----------------------------------")
        temp = self.head
        while temp:
            print(f"Roll No: {temp.roll}, Name: {temp.name}, Marks: {temp.marks}")
            temp = temp.next
        print("-----------------------------------\n")

    # Search Student by Roll No
    def search(self, roll):
        temp = self.head
        while temp:
            if temp.roll == roll:
                print(f"\nRecord Found: Roll No: {temp.roll}, Name: {temp.name}, Marks: {temp.marks}\n")
                return
            temp = temp.next
        print("\nRecord Not Found!\n")

    # Delete Student Record
    def delete(self, roll):
        temp = self.head

        if temp is not None and temp.roll == roll:
            self.head = temp.next
            print("\nRecord Deleted Successfully.\n")
            return

        prev = None
        while temp and temp.roll != roll:
            prev = temp
            temp = temp.next

        if temp is None:
            print("\nRecord Not Found!\n")
            return

        prev.next = temp.next
        print("\nRecord Deleted Successfully.\n")

    # Update Student Marks or Name
    def update(self, roll, new_name=None, new_marks=None):
        temp = self.head
        while temp:
            if temp.roll == roll:
                if new_name:
                    temp.name = new_name
                if new_marks is not None:
                    temp.marks = new_marks
                print("\nRecord Updated Successfully.\n")
                return
            temp = temp.next
        print("\nRecord Not Found!\n")

    # Sort by Marks or Roll No
    def sort_records(self, key="marks", order="asc"):
        if self.head is None:
            print("\nNo Records to Sort.\n")
            return

        swapped = True
        while swapped:
            swapped = False
            temp = self.head
            while temp.next:
                if (order == "asc" and getattr(temp, key) > getattr(temp.next, key)) or \
                   (order == "desc" and getattr(temp, key) < getattr(temp.next, key)):
                    temp.roll, temp.next.roll = temp.next.roll, temp.roll
                    temp.name, temp.next.name = temp.next.name, temp.name
                    temp.marks, temp.next.marks = temp.next.marks, temp.marks
                    swapped = True
                temp = temp.next

        print("\nRecords Sorted Successfully.\n")


# -------------------- DEMO --------------------
obj = StudentList()

obj.add_student(101, "Amit", 85)
obj.add_student(102, "Rahul", 75)
obj.add_student(103, "Sneha", 92)

obj.display()

obj.search(102)

obj.update(102, new_marks=88)
obj.display()

obj.sort_records(key="marks", order="desc")
obj.display()

obj.delete(101)
obj.display()
