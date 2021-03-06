import os
import dotenv
import glob
from random import choice, randint
from entities.trie import TrieTree
from services.input_converter import ShakuConverter
from auxiliary_rules import RuleSet

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
        self.rules = {"pitch": RuleSet(), "lenght": RuleSet()}

    def _populate_trees(self):
        filelist = glob.glob(os.getenv("SHAKUGEN_TRAINING_FILES"))
        converter = ShakuConverter()
        pitches = converter.get_pitch_lists(filelist)
        lenghts = converter.get_lenght_lists(filelist)
        self.pitch_trie.feed_data(pitches)
        self.lenght_trie.feed_data(lenghts)

    def _get_random_start_data(self, type: str) -> int:
        if type == "pitch":
            return choice(self.pitch_range)
        elif type == "lenght":
            lenght = choice(self.lenght_range)
            return(lenght)
        else:
            raise ValueError("Requested unknown type of data")

    def _get_next(self, type: str, previous: list=[]) -> int:
        """Returns a midi integer based on data in trie and data given

        Args:
            type: pitch or lenght of musical note
            previous: List of previous data in sequence. Defaults to an empty string.

        Returns:
            int: Random note if no sequence provided, otherwise note based on previous sequence data
        """

        if len(previous) == 0:
            result = self._get_random_start_data(type)
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
        try:
            index = randint(1, node.repeats["total"])
        except:
            return self._get_random_start_data(type)
        for key, value in node.repeats.items():
            if key == "total":
                continue
            index -= value
            if index <= 0:
                if self.rules[type].repetition_stop(key) < int(os.getenv(type.upper() + "_REP_STOP_WEIGHT")):
                    return key
        return self._get_random_start_data(type)

    def generate_note(self, previous: dict) -> tuple:
        """Return a tuple of pitch and lenght of next note based on given sequence of previous notes

        Args:
            previous (dict): Dictionary representation of previous notes as {
                "pitches" : [list of pitches]
                "lenghts" : [list of lenghts]
            }

        Returns:
            tuple: (pitch, lenght) of generated musical note
        """
        if not previous:
            pitch = self._get_random_start_data("pitch")
            lenght = self._get_random_start_data("lenght")
        else:
            pitch = self._get_next("pitch", previous["pitches"])
            lenght = self._get_next("lenght", previous["lenghts"])
        return (pitch, lenght)
