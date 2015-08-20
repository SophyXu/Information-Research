__author__ = 'xxy'

import pickle

#wordid = -1 means this entry should be eliminated from the result (this word is not indexed)
#input: [[wordid, docid, posi], [wordid, docid, posi] ....]

lists = pickle.load(open('tuples.pickle','rb'))
print((lists))
print(len(lists))

# lists = [[1, 1, 0], [1, 1, 3], [1, 2, 1], [1, 3, 4], [2, 1, 0], [2, 1, 3], [2, 4, 3]]

preWordId = -1
preDocId = -1

dic = {}
wordList = []
docTuple = ()
tf = 0
posList = []

# Iterate lists
for list in lists :
    # print(list)

    # New WordId
    if (preWordId != list[0]) :
        tuple = (preDocId, tf, posList)
        wordList.append(tuple)
        dic[preWordId] = wordList

        # Initialize
        wordList = []
        docTuple = ()

        preWordId = list[0]
        preDocId = list[1]

        tf = 1
        posList = [list[2]]

    else :
        if (list[1] == preDocId) :
            tf = tf + 1
            posList.append(list[2])

        # New DocId
        else :
            tuple = (preDocId, tf, posList)
            wordList.append(tuple)

            # Initialize
            preDocId = list[1]
            tf = 1
            posList = [list[2]]

tuple = (preDocId, tf, posList)
wordList.append(tuple)
dic[preWordId] = wordList

del dic[-1]

pickle.dump(dic, open('c.pickle', 'wb'))
# open("c.temp", 'w').write(str(dic))
# print(dic)

#{wordid: [(docid, tf, [posi] ), (docid2, ....), ....], wordid2: ....}
# 1: [], 2: [] -1 filter
