from random import choice, randint
from trie import TrieTree

class ShakuGenerator:
    """Class for generating musical notes based on previous sequences stored in a trie tree

    Attributes:
        trie: Trie-tree data structure received as constructor parameter
    """
    def __init__(self, trie: TrieTree):
        """Class constructor, saves given trie tree as class attribute"""
        self.trie = trie

    def _get_random_start_note(self):
        pos = list(range(62, 98))
        return choice(pos)

    def generate_note(self, previous=None):
        """Returns a midi integer based on data in trie and data given

        Args:
            previous: List of previous notes after which to generate new note. Defaults to None.

        Raises:
            ValueError: If given sequence is too long (more than 3)

        Returns:
            int: Random note if no sequence provided, otherwise note based on previous sequence data
        """
        if not previous:
            return self._get_random_start_note()
        if len(previous) > 3:
            raise ValueError("Too long sequence given")
        node = self.trie.root
        i = 0
        while i < len(previous):
            if previous[i] not in node.nodes:
                node = self.trie.root
            else:
                node = node.nodes[previous[i]]
            i += 1
        index = randint(1, node.repeats["total"])
        for key, value in node.repeats.items():
            index -= value
            if index <= 0:
                return key
