from main.datastore.triesDS import Tries
from main.datastore.triesData import data


def retrieve():
    testTrie = Tries()
    for i in range(len(data)):
        testTrie[data[i]] = data[i]
    print('TriesDB Initialized as app object')
    return testTrie
