from collections import defaultdict, deque
from string import ascii_lowercase

class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []

        parents = defaultdict(list)
        level = {beginWord}
        found = False

        while level and not found:
            next_level = defaultdict(list)

            for word in level:
                wordSet.discard(word)

            for word in level:
                for i in range(len(word)):
                    for c in ascii_lowercase:
                        newWord = word[:i] + c + word[i + 1:]
                        if newWord in wordSet:
                            next_level[newWord].append(word)
                            if newWord == endWord:
                                found = True

            level = set(next_level.keys())

            for word in next_level:
                parents[word].extend(next_level[word])

        if not found:
            return []

        res = []

        def backtrack(word, path):
            if word == beginWord:
                res.append(path[::-1])
                return
            for parent in parents[word]:
                backtrack(parent, path + [parent])

        backtrack(endWord, [endWord])
        return res