import collections

'''
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]
'''

def ladderLength(beginWord, endWord, wordList):
    wildCardWordToWords = defaultdict(list)
    for i in range(len(beginWord)):
        wildCardWordToWords[beginWord[:i] + '*' + beginWord[i+1:]].append(beginWord)

    for word in wordList:
        for i in range(len(word)):
            wildCardWordToWords[word[:i] + '*' + word[i+1:]].append(word)

    queue = collections.deque([beginWord])
    length = 0
    visited = set()
    while queue:
        currWord = queue.popleft()
        visited.add(currWord)
        length += 1
        for i in range(len(currWord)):
            neighborWords = wildCardWordToWords[currWord[:i] + '*' + currWord[i+1:]]
            for neighborWord in neighborWords:
                if endWord == neighborWord:
                    return length
                if neighborWord not in visited:
                    queue.append(neighborWord)
    return 0