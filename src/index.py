import sys
from generate import ShakuGenerator
from trie import TrieTree

if __name__ == "__main__":
    count = int(sys.argv[1])
    TRAINING_FILE = "training_data.csv"
    with open(TRAINING_FILE, 'r', encoding="utf-8") as f:
        data = f.read().replace("\n", "")
    ints = data.split(",")
    for key in enumerate(ints):
        ints[key] = int(ints[key])
    trie = TrieTree()
    trie.feed_data(ints)
    generator = ShakuGenerator(trie)
    part = []
    while count > 0:
        part.append(str(generator.generate_note()))
        count -= 1
    CSV_VERSION = ",".join(part)
    with open("output.csv", "w", encoding="utf-8") as f:
        f.write(CSV_VERSION)
