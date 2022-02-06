from random import choice, randint
from trie import TrieTree

class ShakuGenerator:
    def __init__(self, trie: TrieTree):
        self.trie = trie

    def _get_random_start_note(self):
        pos = [i for i in range(62, 98)]
        return choice(pos)

    def generate_note(self, previous=None):
        if not previous:
            return self._get_random_start_note()
        node = self.trie
        x = 0
        while x < len(previous) - 1:
            node = node.nodes[previous[x]]
            x += 1
        index = randint(1, node.repeats["total"])
        for key, value in node.repeats.items():
            if key == "total":
                continue
            index -= value
            if index <= 0:
                return key
