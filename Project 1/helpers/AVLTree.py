class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        pass

    def setInterval(self, start, end):
        self.start = start
        self.end = end
        self.ans = 10**9 + 7

    def removeAndInsertNext(self, root, val):
        root = self.delete(root, val)
        if not self.isExists(root, val + 1):
            root = self.insert(root, val + 1)

        return root

    def isExists(self, root, val):
        if root is None:
            return False

        if val == root.data:
            return True

        if val < root.data:
            return self.isExists(root.left, val)

        return self.isExists(root.right, val)

    def getClosestSmallestNode(self, root):
        if root is None:
            return self.ans

        if root.data == self.start:
            self.ans = root.data
        elif root.data < self.start:
            self.getClosestSmallestNode(root.right)
        else:
            if root.data <= self.end:
                self.ans = min(self.ans, root.data)
            self.getClosestSmallestNode(root.left)

        return self.ans

    def height(self, root):
        if root is None:
            return 0

        return root.height

    def balancefactor(self, root):
        if root is None:
            return 0

        return self.height(root.left) - self.height(root.right)

    def insert(self, root, key):
        if root is None:
            return Node(key)

        if key > root.data:
            root.right = self.insert(root.right, key)
        else:
            root.left = self.insert(root.left, key)

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.balancefactor(root)

        # Left - Left
        if balance > 1 and key < root.left.data:
            return self.rotateRight(root)

        # Left-Right
        if balance > 1 and key > root.left.data:
            root.left = self.rotateLeft(root.left)
            return self.rotateRight(root)

        # Right-Right
        if balance < -1 and key > root.right.data:
            return self.rotateLeft(root)

        # Right-Left
        if balance < -1 and key < root.right.data:
            root.right = self.rotateRight(root.right)
            return self.rotateLeft(root)

        return root

    def delete(self, root, key):
        if root is None:
            return root

        if key < root.data:
            root.left = self.delete(root.left, key)

        elif key > root.data:
            root.right = self.delete(root.right, key)

        else:
            if root.left is None:
                return root.right

            elif root.right is None:
                return root.left

            temp = self.getMinNode(root.right)
            root.data = temp.data
            root.right = self.delete(root.right, temp.data)

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.balancefactor(root)

        # Left-Left
        if balance > 1 and self.balancefactor(root.left) >= 0:
            return self.rotateRight(root)

        # Right-Right
        if balance < -1 and self.balancefactor(root.right) <= 0:
            return self.rotateLeft(root)

        # Left-Right
        if balance > 1 and self.balancefactor(root.left) < 0:
            root.left = self.rotateLeft(root.left)
            return self.rotateRight(root)

        # Right-Left
        if balance < -1 and self.balancefactor(root.right) > 0:
            root.right = self.rotateRight(root.right)
            return self.rotateLeft(root)

        return root

    def getMinNode(self, root):
        if root.left is None:
            return root

        return self.getMinNode(root.left)

    def rotateLeft(self, a):
        b = a.right
        bl = b.left
        b.left = a
        a.right = bl

        a.height = 1 + max(self.height(a.left), self.height(a.right))
        b.height = 1 + max(self.height(b.left), self.height(b.right))

        return b

    def rotateRight(self, a):
        b = a.left
        br = b.right
        b.right = a
        a.left = br

        a.height = 1 + max(self.height(a.left), self.height(a.right))
        b.height = 1 + max(self.height(b.left), self.height(b.right))

        return b

    def preOrder(self, root):
        if not root:
            return

        print("{0} ".format(root.data), end="")
        self.preOrder(root.left)
        self.preOrder(root.right)
