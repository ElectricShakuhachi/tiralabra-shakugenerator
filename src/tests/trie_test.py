import unittest
import random
import time
from entities.trie import TrieTree, TrieNode

class TestTrieNode(unittest.TestCase):
    def setUp(self):
        self.node = TrieNode()

    def test_default_init_value_is_none(self):
        self.assertEqual(self.node.value, None)

class TestTrieTree(unittest.TestCase):
    def setUp(self):
        self.trie = TrieTree()

    def _setup_feed_data_20_ints(self):
        data = [[65,64,63,62,63,64,65,63,56,66,63,78,72,66,65,63,65,63,75,73]]
        self.trie.feed_data(data)

    def test_default_parent_node_value_is_none(self):
        self.assertEqual(self.trie.root.value, None)

    def test_initialised_trie_parent_connected_to_no_nodes(self):
        self.assertEqual(len(self.trie.root.nodes), 0)

    def test_add_sequence_raises_on_less_than_four(self):
        self.assertRaises(ValueError, self.trie._add_sequence, ([66,66,55]))

    def test_add_sequence_raises_on_more_than_four(self):
        self.assertRaises(ValueError, self.trie._add_sequence, ([66, 66, 66, 66, 66]))
    
    def _setup_one_correct_sequence(self):
        self.trie._add_sequence([62, 63, 64, 65])

    def test_add_sequence_adds_one_node_connected_to_parent(self):
        self._setup_one_correct_sequence()
        self.assertEqual(len(self.trie.root.nodes), 1)

    def test_add_sequence_adds_one_node_on_second_level(self):
        self._setup_one_correct_sequence()
        node = self.trie.root.nodes[62]
        self.assertEqual(len(node.nodes), 1)

    def test_add_sequence_adds_one_node_on_third_level(self):
        self._setup_one_correct_sequence()
        node = self.trie.root.nodes[62].nodes[63]
        self.assertEqual(len(node.nodes), 1)

    def test_add_sequence_adds_one_node_on_fourth_level(self):
        self._setup_one_correct_sequence()
        node = self.trie.root.nodes[62].nodes[63].nodes[64]
        self.assertEqual(len(node.nodes), 1)

    def test_add_sequence_adds_no_notes_on_fifth_level(self):
        self._setup_one_correct_sequence()
        node = self.trie.root.nodes[62].nodes[63].nodes[64].nodes[65]
        self.assertEqual(len(node.nodes), 0)

    def test_feed_data_doesnt_add_last_three_notes_on_first_level(self):
        self._setup_feed_data_20_ints()
        self.assertEqual(75 in self.trie.root.nodes.keys(), False)

    def test_feed_data_makes_correct_amount_of_nodes_on_first_level(self):
        self._setup_feed_data_20_ints()
        self.assertEqual(len(self.trie.root.nodes), 8)

    def test_feed_data_adds_correct_amount_of_nodes_on_second_level_first_node(self):
        self._setup_feed_data_20_ints()
        node = self.trie.root.nodes[65]
        self.assertEqual(len(node.nodes), 2)

    def test_feed_data_adds_correct_nodes_on_second_level_first_node(self):
        self._setup_feed_data_20_ints()
        node = self.trie.root.nodes[65]
        self.assertEqual(64 in node.nodes and 63 in node.nodes, True)

    def test_feed_data_adds_correct_amount_of_nodes_on_second_level_second_node(self):
        self._setup_feed_data_20_ints()
        node = self.trie.root.nodes[64]
        self.assertEqual(len(node.nodes), 2)

    def test_feed_data_adds_correct_nodes_on_second_level_second_node(self):
        self._setup_feed_data_20_ints()
        node = self.trie.root.nodes[64]
        self.assertEqual(63 in node.nodes and 65 in node.nodes, True)

    def test_feed_data_adds_correct_amount_of_nodes_on_third_level_second_node(self):
        self._setup_feed_data_20_ints()
        node = self.trie.root.nodes[65].nodes[63]
        self.assertEqual(len(node.nodes), 3)

    def test_feed_data_adds_correct_nodes_on_third_level_second_node(self):
        self._setup_feed_data_20_ints()
        node = self.trie.root.nodes[65].nodes[63]
        self.assertEqual(56 in node.nodes and 65 in node.nodes and 75 in node.nodes, True)

    def test_feed_data_adds_correct_amount_of_reps_first_level(self):
        self._setup_feed_data_20_ints()
        total = sum(self.trie.root.repeats.values())
        total -= self.trie.root.repeats["total"]
        self.assertEqual(total, 17)

    def test_feed_data_counts_correct_total_into_reps_first_level(self):
        self._setup_feed_data_20_ints()
        total = sum(self.trie.root.repeats.values())
        total -= self.trie.root.repeats["total"]
        self.assertEqual(total, self.trie.root.repeats["total"])

    def test_feed_data_adds_correct_amount_of_reps_second_level_first_node(self):
        self._setup_feed_data_20_ints()
        node = self.trie.root.nodes[65]
        total = sum(node.repeats.values())
        total -= node.repeats["total"]
        self.assertEqual(total, 4)

    def test_feed_data_counts_correct_total_into_reps_second_level_first_node(self):
        self._setup_feed_data_20_ints()
        node = self.trie.root.nodes[65]
        total = sum(node.repeats.values())
        total -= node.repeats["total"]
        self.assertEqual(total, node.repeats["total"])

    def test_feed_data_time_complexity(self):
        statistics = {}
        for data_count in [1, 2, 4, 8, 16, 32, 64]:
            self.trie = TrieTree()
            training_data = []
            start = time.perf_counter()
            for i in range(data_count * 4):
                training_data.append(random.choice(range(100)))
            end = time.perf_counter()
            statistics[data_count] = end - start
        for i in [2, 4, 8, 16, 32]:
            div1 = statistics[i] / statistics[i // 2]
            div2 = statistics[i * 2] / statistics[i]
            increase_comparison = abs(div2 - div1)
            self.assertGreater(2, increase_comparison)
