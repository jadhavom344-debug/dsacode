class Node:
    def _init_(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks
        self.next = None

class StudentList:
    def _init_(self):
        self.head = None

    def add(self, roll, name, marks):
        new = Node(roll, name, marks)
        if self.head is None:
            self.head = new
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new
        print("Record Added!")

    def display(self):
        if self.head is None:
            print("No Records!")
            return
        print("\nRoll\tName\tMarks")
        temp = self.head
        while temp:
            print(f"{temp.roll}\t{temp.name}\t{temp.marks}")
            temp = temp.next

    def search(self, roll):
        temp = self.head
        while temp:
            if temp.roll == roll:
                print(f"Found -> {temp.roll} {temp.name} {temp.marks}")
                return
            temp = temp.next
        print("Not Found!")

    def sort(self):
        temp = self.head
        while temp:
            nxt = temp.next
            while nxt:
                if temp.marks > nxt.marks:
                    temp.roll, nxt.roll = nxt.roll, temp.roll
                    temp.name, nxt.name = nxt.name, temp.name
                    temp.marks, nxt.marks = nxt.marks, temp.marks
                nxt = nxt.next
            temp = temp.next
        print("Sorted by Marks!")

# ---------- Main ----------
s = StudentList()
while True:
    print("\n1.Add  2.Display  3.Search  4.Sort  5.Exit")
    ch = int(input("Enter choice: "))
    if ch == 1:
        r = int(input("Roll: "))
        n = input("Name: ")
        m = int(input("Marks: "))
        s.add(r, n, m)
    elif ch == 2:
        s.display()
    elif ch == 3:
        r = int(input("Enter Roll: "))
        s.search(r)
    elif ch == 4:
        s.sort()
        s.display()
    elif ch == 5:
        break
