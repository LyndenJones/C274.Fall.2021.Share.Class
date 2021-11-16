import pickle
# BUG import huffman_2021/huffman
# BUG import huffman
from huffman import *

def testmain():
    with open("tree.test.1.pickle", "rb") as fout:
        tree = pickle.load(fout)
    print(tree)
    return


if __name__ == "__main__":
    testmain()
