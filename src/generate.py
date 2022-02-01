from random import choice
from trie import TrieTree

class ShakuGenerator:
    def __init__(self):
        pass

    def _get_random_start_note(self):
        pos = [i for i in range(62, 98)]
        return choice(pos)

    def generate_note(self, previous=None):
        if not previous:
            return self._get_random_start_note()
        else:
            #here we need to handle starts from 1 prev or 2 prev
            #ergo our trie should support probabilities on those.
            #--- zzt... mr. developer goes to change this next... but first... some sleep...
