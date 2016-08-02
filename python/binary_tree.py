class Node:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def __str__(self):
        return "(value: " + str(self.value) + ", left: " + str(self.left) + ", right: " + str(self.right) + ")"

class Tree:
    def __init__(self, root):
        self.root = root

    def insert(self, node, root):
        if root.value > node.value and root.left is None:
            root.left = node
            node.parent = root
            return
        elif root.value < node.value and root.right is None:
            root.right = node
            node.parent = root
            return

        if root.value > node.value:
            self.insert(node, root.left)
        else:
            self.insert(node, root.right)

    def destruct(self):
        # This works in O(n)
        while self.root:
            if self.root.left is None:
                tmp = self.root.right
                print "Destroying " + str(self.root.value)
                del self.root
                self.root = tmp
            else:
                tmpelem = self.root.left
                self.root.left = tmpelem.right
                tmpelem.right = self.root
                self.root = tmpelem

    def __str__(self):
        return str(self.root)
        

t = Tree(Node(5))
t.insert(Node(2), t.root)
t.insert(Node(1), t.root)
t.insert(Node(7), t.root)
t.insert(Node(6), t.root)
t.insert(Node(3), t.root)

print t

t.destruct()
