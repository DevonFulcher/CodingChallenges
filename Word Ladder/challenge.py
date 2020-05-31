# https://leetcode.com/problems/word-ladder/

'''
bfs
starting with begin word, for each word add neighbor nodes for each word that can be transformed to it be switch one letter

canTransform()
'''

def canTransform(wordA, wordB):
    numDifferences = 0
    for letterA, letterB in zip(wordA, wordB):
        if letterA != letterB:
            numDifferences += 1
        if numDifferences > 1:
            break
    return numDifferences == 1

class Node:
    def __init__(self):
        self.val = None
        self.neighbors = None

def ladderLength(beginWord, endWord, wordList):
    currNode = Node()
    currNode.val = beginWord
    queue = []
    neighborWords = filter(lambda word: canTransform(currNode.val, word), wordList)
    currNode.neighbors = neighborWords
    wordList = filter(lambda word: word not in neighborWords, wordList)
    while queue:
        for neighbor in currNode.neighbors:



