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
        if len(previous) > 3:
            raise ValueError("Too long sequence given")
        node = self.trie.root
        x = 0
        while x < len(previous):
            if previous[x] not in node.nodes:
                node = self.trie.root
            else:
                node = node.nodes[previous[x]]
            x += 1
        index = randint(1, node.repeats["total"])
        for key, value in node.repeats.items():
            index -= value
            if index <= 0:
                return key

#Training data has to be large enough to accomodate enough possible
#sequences

#create tests to validate whether training data is adequate

#also make sure documentation explains that in absence of 
#full sequence shorter sequences are utilized