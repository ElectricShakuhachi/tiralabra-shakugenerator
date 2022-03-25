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

    def __str__(self):
        node_string = "Node:\n"
        node_string += f"Repeats: {self.repeats}\n"
        node_string += "Children:\n"
        for node in self.nodes:
            node_string += str(node)
        return node_string

class TrieTree:
    """Trie tree data structure with frequency mapping
    """
    def __init__(self):
        """Class constructor, creates root node
        """
        self.root = TrieNode(None)

    def _add_sequence(self, seq: list):
        if len(seq) != 4:
            raise ValueError("Sequences should contain four values")
        node = self.root
        for value in seq:
            if value not in node.nodes:
                node.repeats[value] = 1
                node.nodes[value] = TrieNode(value)
                node = node.nodes[value]
            else:
                node.repeats[value] += 1
                node = node.nodes[value]

    def _mark_totals(self, node: TrieNode):
        if len(node.repeats) != 0:
            node.repeats["total"] = sum(node.repeats.values())
        for i in node.nodes.values():
            self._mark_totals(i)

    def _feed_one_list(self, midilist: list):
        for i in range(len(midilist) - 3):
            self._add_sequence(midilist[i:i+4])

    def feed_data(self, list_of_midilists: list):
        """Parse data into every sequence of 4 and form a trie tree of them

        Args:
            data (list): list of lists containing MIDI integers
        """
        for midilist in list_of_midilists:
            self._feed_one_list(midilist)
        self._mark_totals(self.root)

    def __str__(self):
        trie_as_string = "################Trie Representation################\n"
        trie_as_string += str(self.root)
        trie_as_string += "##############Trie Representation Ends##############\n"
        return trie_as_string
