import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from avl_tree import AVLTree, AVLNode

class TestAVLTree(unittest.TestCase):

    def setUp(self):
        self.avl_tree = AVLTree()

    def test_insert(self):
        self.avl_tree.root = self.avl_tree.insert(self.avl_tree.root, 'key1', 'value1')
        self.avl_tree.root = self.avl_tree.insert(self.avl_tree.root, 'key2', 'value2')
        self.assertEqual(self.avl_tree.find(self.avl_tree.root, 'key1').value, ['value1'])
        self.assertEqual(self.avl_tree.find(self.avl_tree.root, 'key2').value, ['value2'])

    def test_find(self):
        self.avl_tree.root = self.avl_tree.insert(self.avl_tree.root, 'key1', 'value1')
        self.assertEqual(self.avl_tree.find(self.avl_tree.root, 'key1').value, ['value1'])
        self.assertIsNone(self.avl_tree.find(self.avl_tree.root, 'non_existent_key'))

    def test_find_all(self):
        self.avl_tree.root = self.avl_tree.insert(self.avl_tree.root, 'key1', 'value1')
        self.avl_tree.root = self.avl_tree.insert(self.avl_tree.root, 'key1', 'value2')
        self.assertEqual(self.avl_tree.find_all(self.avl_tree.root, 'key1'), ['value1', 'value2'])

    def test_delete(self):
        self.avl_tree.root = self.avl_tree.insert(self.avl_tree.root, 'key1', 'value1')
        self.avl_tree.root = self.avl_tree.delete(self.avl_tree.root, 'key1')
        self.assertIsNone(self.avl_tree.find(self.avl_tree.root, 'key1'))

    def test_delete_multiple_values(self):
        self.avl_tree.root = self.avl_tree.insert(self.avl_tree.root, 'key1', 'value1')
        self.avl_tree.root = self.avl_tree.insert(self.avl_tree.root, 'key1', 'value2')
        self.avl_tree.root = self.avl_tree.insert(self.avl_tree.root, 'key1', 'value3')
        self.avl_tree.root = self.avl_tree.delete(self.avl_tree.root, 'key1')
        node = self.avl_tree.find(self.avl_tree.root, 'key1')
        self.assertIsNotNone(node)
        self.assertIn('value2', node.value)
        self.assertIn('value3', node.value)
        self.assertEqual(len(node.value), 2)

    def test_right_rotate(self):
        self.avl_tree.root = AVLNode('root', 'root_value')
        self.avl_tree.root.left = AVLNode('left', 'left_value')
        self.avl_tree.root.left.height = 1
        self.avl_tree.root.height = 2
        new_root = self.avl_tree.right_rotate(self.avl_tree.root)
        self.assertEqual(new_root.key, 'left')
        self.assertEqual(new_root.right.key, 'root')

    def test_left_rotate(self):
        self.avl_tree.root = AVLNode('root', 'root_value')
        self.avl_tree.root.right = AVLNode('right', 'right_value')
        self.avl_tree.root.right.height = 1
        self.avl_tree.root.height = 2
        new_root = self.avl_tree.left_rotate(self.avl_tree.root)
        self.assertEqual(new_root.key, 'right')
        self.assertEqual(new_root.left.key, 'root')

    def test_balance_factor(self):
        self.avl_tree.root = AVLNode('root', 'root_value')
        self.avl_tree.root.left = AVLNode('left', 'left_value')
        self.avl_tree.root.right = AVLNode('right', 'right_value')
        self.avl_tree.root.left.height = 2
        self.avl_tree.root.right.height = 1
        self.avl_tree.root.height = 3
        self.assertEqual(self.avl_tree.balance_factor(self.avl_tree.root), 1)

    def test_height(self):
        self.avl_tree.root = AVLNode('root', 'root_value')
        self.avl_tree.root.left = AVLNode('left', 'left_value')
        self.avl_tree.root.right = AVLNode('right', 'right_value')
        self.avl_tree.root.left.height = 2
        self.avl_tree.root.right.height = 1
        self.avl_tree.root.height = 3
        self.assertEqual(self.avl_tree.height(self.avl_tree.root), 3)

    def test_min_value_node(self):
        self.avl_tree.root = AVLNode('root', 'root_value')
        self.avl_tree.root.left = AVLNode('left', 'left_value')
        self.avl_tree.root.right = AVLNode('right', 'right_value')
        min_node = self.avl_tree.min_value_node(self.avl_tree.root)
        self.assertEqual(min_node.key, 'left')
    
if __name__ == '__main__':
    unittest.main()