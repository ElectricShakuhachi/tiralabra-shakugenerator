import unittest
import random
import time
from shaku_generator import ShakuGenerator
from entities.trie import TrieTree

class TestShakuGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = ShakuGenerator()
        self.pitch_trie = TrieTree()
        self.lenght_trie = TrieTree()
        self.generator.pitch_trie = self.pitch_trie
        self.generator.lenght_trie = self.lenght_trie
        pitches = []
        lenghts = []
        for i in range(25):
            pitches.append(random.choice(range(1, 100)))
            lenghts.append(random.choice(range(1, 64)))
        self.generator.pitch_trie.feed_data([pitches])
        self.generator.lenght_trie.feed_data([lenghts])

    def test_get_random_start_note_gives_values_between_1_and_37(self):
        values = []
        for i in range(500):
            values.append(self.generator._get_random_start_data("pitch"))
        test_var = True
        for note in values:
            if note < 1 or note > 37:
                test_var = False
        self.assertEqual(test_var, True)

    def test_get_random_start_note_gives_various_values(self):
        values = set()
        for i in range(500):
            values.add(self.generator._get_random_start_data("pitch"))
        self.assertGreater(len(values), 5)

    def test_generate_note_returns_random_note_if_no_previous(self):
        values = set()
        for i in range(500):
            values.add(self.generator.generate_note(None))
        self.assertGreater(len(values), 5)

    def test_generate_note_returns_random_note_if_one_previous_with_no_match(self):
        values = set()
        previous = {"pitches": [101], "lenghts": [200]}
        for i in range(500):
            values.add(self.generator.generate_note(previous))
        self.assertGreater(len(values), 5)

    def test_generate_note_returns_various_notes_if_one_previous_with_match(self):
        values = set()
        previous = {"pitches": [89], "lenghts": [4]}
        for i in range(500):
            values.add(self.generator.generate_note(previous))
        self.assertGreater(len(values), 5)

    def _make_defined_trie(self):
        self.generator.pitch_trie = TrieTree()
        self.generator.lenght_trie = TrieTree()
        pitches = []
        lenghts = []
        for i in range(2, 100):
            pitches.append(i)
            lenghts.append(i)
        for pitch, lenght in [(6, 1), (1, 2), (5, 2), (10, 4), (8, 2)]: # set 1
            pitches.append(pitch)
            lenghts.append(lenght)
        for pitch, lenght in [(101, 2), (8, 8), (2, 16), (9, 4), (101, 2), (8, 8), (2, 16), (4, 2)]: # set 2
            pitches.append(pitch)
            lenghts.append(lenght)
        for pitch, lenght in [(102, 9), (60, 16), (20, 32), (38, 16), 
                                (102, 9), (60, 16), (20, 32), (38, 16), 
                                (102, 9), (60, 16), (20, 32), (48, 2),]: # set 3
            pitches.append(pitch)
            lenghts.append(lenght)
        self.generator.pitch_trie.feed_data([pitches])
        self.generator.lenght_trie.feed_data([lenghts])

    def test_generate_note_always_returns_the_right_note_if_there_is_just_one_match_in_trie(self):
        """This test case reflects if algorithm will always return the matched note
        if only one note matches as following the given sequence in trie.
        Utilizes set 1 in _make_defined_trie -method"""
        values = set()
        previous = {"pitches": [1, 5, 10], "lenghts": [2, 2, 4]}
        for i in range(50):
            self.generator = ShakuGenerator()
            self._make_defined_trie()
            values.add(self.generator.generate_note(previous)[0])
        self.assertEqual(len(values) == 1 and 8 in values, True)

    def test_generate_note_generates_note_based_on_last_three_if_four_previous(self):
        self._make_defined_trie()
        previous = {"pitches": [8, 1, 5, 10], "lenghts": [8, 2, 2, 4]}
        self.assertEqual((8, 2), self.generator.generate_note(previous))

    def test_generate_note_returns_random_integer_from_data_if_zero_match_one_prev(self):
        values = set()
        previous = {"pitches": [101], "lenghts": [100]}
        for i in range(5000):
            values.add(self.generator.generate_note(previous))
        self.assertGreater(len(values), 100)

    def test_generate_note_returns_both_possibilities_on_two_matches_test_one(self):
        """Utilizes set 2 in _make_defined_trie -method"""
        values = set()
        previous = {"pitches": [101, 8, 2], "lenghts": [2, 8, 16]}
        for i in range(50):
            self.generator = ShakuGenerator()
            self._make_defined_trie()
            values.add(self.generator.generate_note(previous)[0])
        self.assertEqual(len(values) == 2 and 9 in values and 4 in values, True)

    def test_generate_note_returns_more_represented_note_more_often(self):
        """Utilizes set 3 in _make_defined_trie -method
        Shows that more represented sequence in trie is more likely to be followed
        This test also shows how pitch and trie generation is independent"""
        values = {}
        previous = {"pitches": [102, 60, 20], "lenghts": [60, 10, 20]}
        for i in range(50):
            self.generator = ShakuGenerator()
            self._make_defined_trie()
            note = self.generator.generate_note(previous)[0]
            if note in values:
                values[note] += 1
            else:
                values[note] = 1
        self.assertGreater(values[38], values[48])

    def test_generate_note_exact_variance_differs_per_run(self):
        """Utilizes set 3 in _make_defined_trie method
        Shows that note generation is random to a degree"""
        values1 = {}
        previous = {"pitches": [102, 60, 20], "lenghts": [60, 10, 20]}
        for i in range(1000):
            self.generator = ShakuGenerator()
            self._make_defined_trie()
            note = self.generator.generate_note(previous)[0]
            if note in values1:
                values1[note] += 1
            else:
                values1[note] = 1
        values2 = {}
        for i in range(1000):
            self.generator = ShakuGenerator()
            self._make_defined_trie()
            note = self.generator.generate_note(previous)[0]
            if note in values2:
                values2[note] += 1
            else:
                values2[note] = 1
        self.assertNotEqual(values1[38], values2[38])

    def test_generate_note_time_complexity(self):
        statistics = {}
        for note_count in [1, 2, 4, 8, 16, 32, 64]:
            start = time.perf_counter()
            for repeats in range(note_count):
                previous = []
                note = self.generator.generate_note(previous)
                previous.append(note)
            end = time.perf_counter()
            statistics[note_count] = end - start
        for i in [2, 4, 8, 16, 32]:
            div1 = statistics[i] / statistics[i // 2]
            div2 = statistics[i * 2] / statistics[i]
            increase_comparison = abs(div2 - div1)
            self.assertGreater(2, increase_comparison)
