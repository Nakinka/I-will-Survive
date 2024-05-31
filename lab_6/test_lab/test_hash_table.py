import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from avl_tree import AVLTree, AVLNode
from hash_table import HashTable

class TestHashTable(unittest.TestCase):

    def setUp(self):
        self.hash_table = HashTable()

    def test_create(self):
        self.hash_table.create('key1', 'value1')
        self.assertEqual(self.hash_table.read('key1'), ['value1'])

    def test_update(self):
        self.hash_table.create('key1', 'value1')
        self.hash_table.update('key1', 'new_value1')
        self.assertEqual(self.hash_table.read('key1'), ['new_value1'])

    def test_delete(self):
        self.hash_table.create('key1', 'value1')
        self.hash_table.delete('key1')
        self.assertEqual(self.hash_table.read('key1'), [])

    def test_read_nonexistent_key(self):
        self.assertEqual(self.hash_table.read('nonexistent_key'), [])

    def test_collision(self):
        self.hash_table.create('abc', 'value1')
        self.hash_table.create('cba', 'value2')
        self.assertEqual(self.hash_table.read('abc'), ['value1'])
        self.assertEqual(self.hash_table.read('cba'), ['value2'])

if __name__ == '__main__':
    unittest.main()
