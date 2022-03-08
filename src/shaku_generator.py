import os
import dotenv
import glob
from random import choice, randint
from entities.trie import TrieTree
from services.input_converter import ShakuConverter
from auxiliary_rules import Ruleset

class ShakuGenerator:
    """Class for generating musical notes based on previous sequences stored in a trie tree

    Attributes:
        trie: Trie-tree data structure received as constructor parameter
    """
    def __init__(self):
        dirname = os.path.dirname(__file__)
        dotenv.load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
        self.pitch_trie = TrieTree()
        self.lenght_trie = TrieTree()
        self._populate_trees()
        self.pitch_range = list(range(int(os.getenv("SHAKUGEN_LOWEST_PITCH")), int(os.getenv("SHAKUGEN_HIGHEST_PITCH"))+1))
        self.lenght_range = [int(i) for i in os.getenv("SHAKUGEN_LENGHTS").split(",")]
        self.auxiliary_rules = RuleSet()

    def _populate_trees(self):
        filelist = glob.glob(os.getenv("SHAKUGEN_TRAINING_FILES"))
        converter = ShakuConverter()
        pitches = converter.get_pitch_lists(filelist)
        lenghts = converter.get_lenght_lists(filelist)
        self.pitch_trie.feed_data(pitches)
        self.lenght_trie.feed_data(lenghts)

    def _get_random_start_data(self, type: str):
        if type == "pitch":
            return choice(self.pitch_range)
        elif type == "lenght":
            thing = choice(self.lenght_range)
            return(thing)
        else:
            raise ValueError("Requested unknown type of data")

    def _get_next(self, type: str, previous: list=[]):
        """Returns a midi integer based on data in trie and data given

        Args:
            type: pitch if type of data retrieved is a pitch, lenght if lenght
            previous: List of previous data in sequence. Defaults to None.

        Raises:
            ValueError: If given sequence is too long (more than 3)

        Returns:
            int: Random note if no sequence provided, otherwise note based on previous sequence data
        """

        if len(previous) == 0:
            result = self._get_random_start_data(type)
            self.auxiliary_rules.add_note(result)
            return result
        if len(previous) > 3:
            previous = previous[-3:]
        if type == "pitch":
            trie = self.pitch_trie
        elif type == "lenght":
            trie = self.lenght_trie
        else:
            raise ValueError("Unknown type of data requested")
        node = trie.root
        i = 0
        while i < len(previous):
            if previous[i] not in node.nodes:
                node = trie.root
            else:
                node = node.nodes[previous[i]]
            i += 1
        # trie tree seems to be empty - causing this error - problem in populating trees likely responsible.
        try:
            index = randint(1, node.repeats["total"])
        except:
            raise ValueError("Training data likely insufficient in trie")
        for key, value in node.repeats.items():
            index -= value
            if index <= 0:
                self.auxiliary_rules.add_note(key)
                return key

    def generate_note(self, previous: dict):
        pitch = self._get_next("pitch", previous["pitches"])
        lenght = self._get_next("lenght", previous["lenghts"])
        return (pitch, lenght)
