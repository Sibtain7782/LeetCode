class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        next1 = 1      # dp[n]
        next2 = 0      # dp[n+1] (dummy)

        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                curr = 0
            else:
                curr = next1

                if (i + 1 < n and
                    (s[i] == '1' or
                     (s[i] == '2' and s[i + 1] <= '6'))):
                    curr += next2 if i + 2 <= n else 1

            next2 = next1
            next1 = curr

        return next1