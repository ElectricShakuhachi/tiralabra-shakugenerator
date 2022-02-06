class TrieNode:
    def __init__(self, value=None):
        self.value = value
        self.nodes = {}
        self.repeats = {}

class TrieTree:
    def __init__(self):
        self.root = TrieNode(None)

    def __str__(self):
        stringed = ""
        for i in self.trie.nodes:
            stringed += str(i)

    def _add_sequence(self, seq):
        if len(seq) != 4:
            raise ValueError("Sequences should contain four values")
        x = 0
        node = self.root
        while x < 4:
            if seq[x] not in node.nodes:
                node.repeats[seq[x]] = 1
                node.nodes[seq[x]] = TrieNode(seq[x])
                node = node.nodes[seq[x]]
            else:
                node.repeats[seq[x]] += 1
                node = node.nodes[seq[x]]
            x += 1

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
