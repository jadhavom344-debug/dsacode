class Node:
    def _init_(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def _init_(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, root, value):
        if root is None:
            return Node(value)
        if value < root.value:
            root.left = self._insert(root.left, value)
        else:
            root.right = self._insert(root.right, value)
        return root

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if root is None or root.value == key:
            return root
        if key < root.value:
            return self._search(root.left, key)
        return self._search(root.right, key)

    def inorder(self):
        self._inorder(self.root)
        print()

    def _inorder(self, root):
        if root:
            self._inorder(root.left)
            print(root.value, end=" ")
            self._inorder(root.right)

    def delete(self, value):
        self.root = self._delete(self.root, value)

    def _delete(self, root, key):
        if root is None:
            return root

        if key < root.value:
            root.left = self._delete(root.left, key)
        elif key > root.value:
            root.right = self._delete(root.right, key)
        else:
            # Case 1 & Case 2
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Case 3: Two children
            successor = self._min_value_node(root.right)
            root.value = successor.value
            root.right = self._delete(root.right, successor.value)

        return root

    def _min_value_node(self, node):
        while node.left:
            node = node.left
        return node


# Driver Code
bst = BST()
elements = [50, 30, 70, 20, 40, 60, 80]

print("Inserting elements:", elements)
for e in elements:
    bst.insert(e)

print("Inorder Traversal:")
bst.inorder()

key = 40
print(f"Searching for {key}:", "Found" if bst.search(key) else "Not Found")

delete_key = 30
print(f"Deleting {delete_key}")
bst.delete(delete_key)

print("Inorder Traversal after deletion:")
bst.inorder()
