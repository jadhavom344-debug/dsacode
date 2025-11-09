# Program: Undo/Redo System using Stack

undo_stack = []
redo_stack = []
document = ""  # current state of document

def make_change(new_text):
    global document
    undo_stack.append(document)
    document = new_text
    redo_stack.clear()
    print("Change made.")

def undo():
    global document
    if undo_stack:
        redo_stack.append(document)
        document = undo_stack.pop()
        print("Undo performed.")
    else:
        print("Nothing to undo!")

def redo():
    global document
    if redo_stack:
        undo_stack.append(document)
        document = redo_stack.pop()
        print("Redo performed.")
    else:
        print("Nothing to redo!")

def display():
    print("Current Document State:", document)

# --- Testing the system ---
make_change("Version 1: Hello")
make_change("Version 2: Hello World")
make_change("Version 3: Hello World!!!")

display()

undo()      # Undo last change
display()

redo()      # Redo last undone change
display()
