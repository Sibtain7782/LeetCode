class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        # pal[i][j] = True if s[i:j+1] is a palindrome
        pal = [[False] * n for _ in range(n)]

        for i in range(n):
            pal[i][i] = True

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                if s[i] == s[j]:
                    if length == 2 or pal[i + 1][j - 1]:
                        pal[i][j] = True

        # dp[i] = maximum number of substrings in s[:i]
        dp = [0] * (n + 1)

        for j in range(n):
            # Don't use a palindrome ending at j
            dp[j + 1] = dp[j]

            for i in range(j + 1):
                length = j - i + 1

                if length >= k and pal[i][j]:
                    dp[j + 1] = max(dp[j + 1], dp[i] + 1)

        return dp[n]