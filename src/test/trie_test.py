import unittest
from trie import TrieTree, TrieNode

class TestTrieNode(unittest.TestCase):
    def setUp(self):
        self.node = TrieNode()

    def test_default_init_value_is_none(self):
        self.assertEqual(self.node.value, None)

class TestTrieTree(unittest.TestCase):
    def setUp(self):
        self.trie = TrieTree()

    def test_default_parent_node_value_is_none(self):
        self.assertEqual(self.trie.trie.value, None)

    def test_initialised_trie_connected_to_no_nodes(self):
        self.assertEqual(len(self.trie.trie.nodes), 0)

    def test_add_sequence_raises_on_less_than_four(self):
        self.assertRaises(ValueError, self.trie._add_sequence, ([66,66,55]))

    def test_add_sequence_raises_on_more_than_four(self):
        self.assertRaises(ValueError, self.trie._add_sequence, ([66, 66, 66, 66, 66]))
    
    def test_add_sequence_adds_one_node_connected_to_parent(self):
        self.assertEqual(len(self.trie.trie.nodes), 1)

    def test_add_sequence_adds_one_node_on_second_level(self):
        node = self.trie.trie.nodes.values()[0]
        self.assertEqual(len(node.nodes), 1)

    def test_add_sequence_adds_one_node_on_third_level(self):
        node = self.trie.trie.nodes.values()[0].nodes.values()[0]
        self.assertEqual(len(node.nodes), 1)

    def test_add_sequence_adds_one_node_on_fourth_level(self):
        node = self.trie.trie.nodes.values()[0].nodes.values()[0].nodes.values()[0]
        self.assertEqual(len(node.nodes), 1)
        