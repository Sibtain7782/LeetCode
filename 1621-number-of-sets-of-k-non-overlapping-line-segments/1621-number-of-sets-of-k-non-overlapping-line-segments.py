class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        # dp[j][i] = number of ways to draw j segments
        # using points 0 ... i
        dp = [[0] * n for _ in range(k + 1)]

        # With 0 segments, there is exactly 1 way.
        for i in range(n):
            dp[0][i] = 1

        for j in range(1, k + 1):
            prefix = 0

            for i in range(1, n):
                # Sum dp[j-1][p] for all possible starting points p <= i-1
                prefix = (prefix + dp[j - 1][i - 1]) % MOD

                # We can:
                # 1. Not use point i as the right endpoint
                # 2. End a segment at i
                #
                # If segment starts at p, previous segments must end <= p.
                dp[j][i] = (dp[j][i - 1] + prefix) % MOD

        return dp[k][n - 1]