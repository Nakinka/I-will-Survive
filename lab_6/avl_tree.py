class AVLNode:
    def __init__(self, key, value):
        self.key = key
        self.value = [value]  
        self.height = 1
        self.left = None
        self.right = None


class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if node is None:
            return 0
        return node.height

    def balance_factor(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def right_rotate(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self.height(y.left), self.height(y.right))
        x.height = 1 + max(self.height(x.left), self.height(x.right))

        return x

    def left_rotate(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = 1 + max(self.height(x.left), self.height(x.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def insert(self, root, key, value):
        if root is None:
            return AVLNode(key, value)
        elif key < root.key:
            root.left = self.insert(root.left, key, value)
        elif key > root.key:
            root.right = self.insert(root.right, key, value)
        else:
            root.value.append(value)  

        root.height = 1 + max(self.height(root.left), self.height(root.right))

        balance = self.balance_factor(root)

        if balance > 1:
            if key < root.left.key:
                return self.right_rotate(root)
            else:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)

        if balance < -1:
            if key > root.right.key:
                return self.left_rotate(root)
            else:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)

        return root

    def find(self, root, key):
        if root is None or root.key == key:
            return root

        if root.key < key:
            return self.find(root.right, key)

        return self.find(root.left, key)

    def find_all(self, root, key):
        values = []
        self._find_all_helper(root, key, values)
        return values

    def _find_all_helper(self, root, key, values):
        if root is None:
            return
        if root.key == key:
            values.extend(root.value)
        if root.key <= key:
            self._find_all_helper(root.right, key, values)
        if root.key >= key:
            self._find_all_helper(root.left, key, values)

    def in_order_traversal(self, root):
        if root is not None:
            self.in_order_traversal(root.left)
            print(f"({root.key}, {root.value})")
            self.in_order_traversal(root.right)

    def min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    

    def delete(self, root, key):
        if root is None:
            return root
        elif key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if len(root.value) > 1:
                root.value.pop(0)
                return root
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.min_value_node(root.right)
            root.key = temp.key
            root.value = temp.value
            root.right = self.delete(root.right, temp.key)

        root.height = 1 + max(self.height(root.left), self.height(root.right))


        balance = self.balance_factor(root)

        # ЛЛ
        if balance > 1 and self.balance_factor(root.left) >= 0:
            return self.right_rotate(root)

        # ПП
        if balance < -1 and self.balance_factor(root.right) <= 0:
            return self.left_rotate(root)

        # ЛП
        if balance > 1 and self.balance_factor(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # ПЛ
        if balance < -1 and self.balance_factor(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root
