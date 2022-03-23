import unittest
import random
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
        for pitch, lenght in [(1, 2), (5, 2), (10, 4), (8, 2)]:
            pitches.append(pitch)
            lenghts.append(lenght)
        self.generator.pitch_trie.feed_data([pitches])
        self.generator.lenght_trie.feed_data([lenghts])

    def test_generate_note_always_returns_the_right_note_if_there_is_just_one_match_in_trie(self):
        values = []
        previous = {"pitches": [1, 5, 10], "lenghts": [2, 2, 4]}
        for i in range(50):
            self.generator = ShakuGenerator()
            self._make_defined_trie()
            values.append(self.generator.generate_note(previous))
        pitch_count = 0
        lenght_count = 0
        for note in values:
            if note[0] == 8:
                pitch_count += 1
            if note[1] == 2:
                lenght_count += 1
        self.assertEqual(pitch_count, 50)

    # def test_generate_note_returns_one_integer_if_three_previous_with_match(self):
    #     self.assertIsInstance(self.generator.generate_note([65,63,62]), int)

    # def test_generate_note_returns_error_if_four_previous_given(self):
    #     self.assertRaises(ValueError, self.generator.generate_note, ([65,63,62,63]))

    # def test_generate_note_returns_error_if_five_previous_given(self):
    #     self.assertRaises(ValueError, self.generator.generate_note, ([65,63,62,62,63]))

    # def test_generate_note_returns_random_integer_from_data_if_zero_match_one_prev(self):
    #     values = set()
    #     for i in range(50000):
    #         values.add(self.generator.generate_note([93]))
    #     self.assertEqual(len(values), 9)

    # def test_generate_note_returns_random_integer_from_data_if_zero_match_two_prev(self):
    #     values = set()
    #     for i in range(50000):
    #         values.add(self.generator.generate_note([93,91]))
    #     self.assertEqual(len(values), 9)

    # def test_generate_note_returns_correct_note_on_one_match_test_one(self):
    #     note = self.generator.generate_note([62,65,65])
    #     self.assertEqual(note, 63)

    # def test_generate_note_returns_correct_note_on_one_match_test_two(self):
    #     note = self.generator.generate_note([62,62,63])
    #     self.assertEqual(note, 64)

    # def test_generate_note_returns_correct_note_on_one_match_two_prev(self):
    #     note = self.generator.generate_note([62,62])
    #     self.assertEqual(note, 63)

    # def test_generate_note_returns_both_possibilities_on_two_matches_test_one(self):
    #     values = set()
    #     for i in range(100):
    #         values.add(self.generator.generate_note([63, 63, 63]))
    #     self.assertEqual(61 in values and 80 in values, True)

    # def test_generate_note_returns_two_different_values_on_two_matches_test_one(self):
    #     values = set()
    #     for i in range(100):
    #         values.add(self.generator.generate_note([63, 63, 63]))
    #     self.assertEqual(len(values), 2)

    # def test_generate_note_returns_more_likely_value_more_often(self):
    #     count_80 = 0
    #     count_61 = 0
    #     for i in range(100):
    #         value = self.generator.generate_note([63, 63, 63])
    #         if value == 80:
    #             count_80 += 1
    #         elif value == 61:
    #             count_61 += 1
    #     self.assertGreater(count_80, count_61)

    # def test_generate_note_exact_variance_differs_per_run(self):
    #     count_80_first = 0
    #     count_80_second = 0
    #     for i in range(10000):
    #         value = self.generator.generate_note([63, 63, 63])
    #         if value == 80:
    #             count_80_first += 1
    #     for i in range(10000):
    #         value = self.generator.generate_note([63,63,63])
    #         if value == 80:
    #             count_80_second += 1
    #     self.assertNotEqual(count_80_first, count_80_second)

    # def test_generate_note_returns_exact_match_to_second_level_one_match(self):
    #     self.assertEqual(self.generator.generate_note([90,90,67]), 89)
