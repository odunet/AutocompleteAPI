from main.triesDB.classDS import Tries
import pickle

with open('main/triesDB/data/rawData/completePickleData.pkl', 'rb') as f:
# with open('data/rawData/completePickleData.pkl', 'rb') as f:
    data = pickle.load(f)

def retrieve():
    testTrie = Tries()
    for i in range(len(data)):
        testTrie[data[i]] = data[i]
    print('TriesDB Initialized a Flask-App object')
    return testTrie
