class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        wordSet = set(wordDict)
        memo = {}

        def dfs(start):
            # Agar result pehle calculate ho chuka hai
            if start in memo:
                return memo[start]

            # String complete ho gayi
            if start == len(s):
                return [""]

            result = []

            # Different words try karo
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]

                if word in wordSet:
                    # Remaining string solve karo
                    for sentence in dfs(end):
                        if sentence:
                            result.append(word + " " + sentence)
                        else:
                            result.append(word)

            memo[start] = result
            return result

        return dfs(0)