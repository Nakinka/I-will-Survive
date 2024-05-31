from avl_tree import AVLTree, AVLNode

class HashTable:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.table = [AVLTree() for _ in range(capacity)]

    def hash_function(self, key):
        hash_value = 0
        for char in str(key):
            hash_value += ord(char)
        return hash_value % self.capacity


    def create(self, key, value):
        index = self.hash_function(key)
        self.table[index].root = self.table[index].insert(self.table[index].root, key, value)


    

    def update(self, key, value):
        index = self.hash_function(key)
       
        self.table[index].root = self.table[index].delete(self.table[index].root, key)
        self.table[index].root = self.table[index].insert(self.table[index].root, key, value)

    def delete(self, key):
        index = self.hash_function(key)
        self.table[index].root = self.table[index].delete(self.table[index].root, key)

    def print_table(self):
        print("HashTable contents:")
        for i, avl_tree in enumerate(self.table):
            print(f"Index {i}:")
            avl_tree.in_order_traversal(avl_tree.root)
            print()

    def read(self, key):
        index = self.hash_function(key)
        return self.table[index].find_all(self.table[index].root, key)
