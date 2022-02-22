class TrieNode:
    """Node in a trie tree

    Attributes:
        value: MIDI integer representing note
        nodes: Dictionary mapping midi ints to instances of TrieNode
        repeats: Dictionary mapping notes to their frequency in sequence
    """
    def __init__(self, value=None):
        """Class constructor, inits attributes

        Args:
            value: MIDI number of note. Defaults to None - only be the case with root node.
        """
        self.value = value
        self.nodes = {}
        self.repeats = {}

class TrieTree:
    """Trie tree data structure with frequency mapping
    """
    def __init__(self):
        """Class constructor, creates root node
        """
        self.root = TrieNode(None)

    def _add_sequence(self, seq):
        if len(seq) != 4:
            raise ValueError("Sequences should contain four values")
        i = 0
        node = self.root
        while i < 4:
            if seq[i] not in node.nodes.items():
                node.repeats[seq[i]] = 1
                node.nodes[seq[i]] = TrieNode(seq[i])
                node = node.nodes[seq[i]]
            else:
                node.repeats[seq[i]] += 1
                node = node.nodes[seq[i]]
            i += 1

    def _mark_probabilities(self, node):
        if len(node.repeats) != 0:
            node.repeats["total"] = sum(node.repeats.values())
        for i in node.nodes.values():
            self._mark_probabilities(i)

    def feed_data(self, data):
        """Parse data into every sequence of 4 and form a trie tree of them

        Args:
            data (list): MIDI integers
        """
        for i in range(len(data) - 3):
            self._add_sequence(data[i:i+4])
        self._mark_probabilities(self.root)
