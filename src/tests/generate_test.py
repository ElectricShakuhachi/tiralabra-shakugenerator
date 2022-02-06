import unittest
from generate import ShakuGenerator
from trie import TrieTree

class TestShakuGenerator(unittest.TestCase):
    def setUp(self):
        data = [62,65,65,63,62,62,63,64,62,67,89,65,83,63,63,63,61,63,63,63,80,63,63,63,80]
        self.trie = TrieTree()
        self.trie.feed_data(data)
        self.generator = ShakuGenerator(self.trie)

    def test_get_random_start_note_gives_values_between_62_98(self):
        values = []
        for i in range(50000):
            values.append(self.generator._get_random_start_note())
        test_var = True
        for note in values:
            if note < 62 or note > 98:
                test_var = False
        self.assertEqual(test_var, True)

    def test_get_random_start_note_gives_various_values(self):
        values = set()
        for i in range(50000):
            values.add(self.generator._get_random_start_note())
        self.assertGreater(len(values), 20)

    def test_generate_note_returns_random_note_if_no_previous(self):
        values = set()
        for i in range(50000):
            values.add(self.generator.generate_note())
        self.assertGreater(len(values), 20)

    def test_generate_note_returns_one_integer_if_no_previous(self):
        self.assertIsInstance(self.generator.generate_note(), int)

    def test_generate_note_returns_one_integer_if_one_previous_with_match(self):
        self.assertIsInstance(self.generator.generate_note([65]), int)

    def test_generate_note_returns_one_integer_if_two_previous_with_match(self):
        self.assertIsInstance(self.generator.generate_note([65,65]), int)

    def test_generate_note_returns_one_integer_if_three_previous_with_match(self):
        self.assertIsInstance(self.generator.generate_note([65,63,62]), int)

    def test_generate_note_returns_error_if_four_previous_given(self):
        self.assertRaises(ValueError, self.generator.generate_note, ([65,63,62,63]))

    def test_generate_note_returns_error_if_five_previous_given(self):
        self.assertRaises(ValueError, self.generator.generate_note, ([65,63,62,62,63]))

    def test_generate_note_returns_random_integer_from_data_if_zero_match_one_prev(self):
        values = set()
        for i in range(50000):
            values.add(self.generator.generate_note([93]))
        self.assertEqual(len(values), 9)

    def test_generate_note_returns_random_integer_from_data_if_zero_match_two_prev(self):
        values = set()
        for i in range(50000):
            values.add(self.generator.generate_note([93,91]))
        self.assertEqual(len(values), 9)

    def test_generate_note_returns_correct_note_on_one_match_test_one(self):
        note = self.generator.generate_note([62,65,65])
        self.assertEqual(note, 63)

    def test_generate_note_returns_correct_note_on_one_match_test_two(self):
        note = self.generator.generate_note([62,62,63])
        self.assertEqual(note, 64)

    def test_generate_note_returns_correct_note_on_one_match_two_prev(self):
        note = self.generator.generate_note([62,62])
        self.assertEqual(note, 63)

    def test_generate_note_returns_both_possibilities_on_two_matches_test_one(self):
        values = set()
        for i in range(100):
            values.add(self.generator.generate_note([63, 63, 63]))
        self.assertEqual(61 in values and 80 in values, True)

    def test_generate_note_returns_two_different_values_on_two_matches_test_one(self):
        values = set()
        for i in range(100):
            values.add(self.generator.generate_note([63, 63, 63]))
        self.assertEqual(len(values), 2)

    def test_generate_note_returns_more_likely_value_more_often(self):
        count_80 = 0
        count_61 = 0
        for i in range(100):
            value = self.generator.generate_note([63, 63, 63])
            if value == 80:
                count_80 += 1
            elif value == 61:
                count_61 += 1
        self.assertGreater(count_80, count_61)

    def test_generate_note_exact_variance_differs_per_run(self):
        count_80_first = 0
        count_80_second = 0
        for i in range(10000):
            value = self.generator.generate_note([63, 63, 63])
            if value == 80:
                count_80_first += 1
        for i in range(10000):
            value = self.generator.generate_note([63,63,63])
            if value == 80:
                count_80_second += 1
        self.assertNotEqual(count_80_first, count_80_second)

    def test_generate_note_returns_exact_match_to_second_level_one_match(self):
        self.assertEqual(self.generator.generate_note([90,90,67]), 89)
