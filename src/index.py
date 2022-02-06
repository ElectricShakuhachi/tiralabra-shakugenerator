from generate import ShakuGenerator
from trie import TrieTree

if __name__ == "__main__":
    file = "training_data.csv"
    with open(file, 'r') as f:
        data = f.read().replace("\n", "")
    ints = data.split(",")
    for i in range(len(ints)):
        ints[i] = int(ints[i])
    trie = TrieTree()
    trie.feed_data(ints)
    #generator = ShakuGenerator(trie)
    #print("Note:")
    #print(generator.generate_note())