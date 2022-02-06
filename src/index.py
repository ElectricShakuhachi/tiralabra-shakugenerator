import sys
from generate import ShakuGenerator
from trie import TrieTree

if __name__ == "__main__":
    count = int(sys.argv[1])
    file = "training_data.csv"
    with open(file, 'r') as f:
        data = f.read().replace("\n", "")
    ints = data.split(",")
    for i in range(len(ints)):
        ints[i] = int(ints[i])
    trie = TrieTree()
    trie.feed_data(ints)
    generator = ShakuGenerator(trie)
    part = []
    while count > 0:
        part.append(str(generator.generate_note()))
        count -= 1
    csv_version = ",".join(part)
    with open("output.csv", "w") as file:
        file.write(csv_version)
