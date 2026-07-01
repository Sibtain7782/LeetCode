class Solution:
    def longestDupSubstring(self, s: str) -> str:
        n = len(s)
        nums = [ord(c) - ord('a') for c in s]

        base = 26
        mod = (1 << 61) - 1

        def search(length):
            h = 0
            for i in range(length):
                h = (h * base + nums[i]) % mod

            seen = {h}
            power = pow(base, length, mod)

            for start in range(1, n - length + 1):
                h = (h * base - nums[start - 1] * power + nums[start + length - 1]) % mod
                h %= mod
                if h in seen:
                    return start
                seen.add(h)
            return -1

        left, right = 1, n - 1
        start = -1
        max_len = 0

        while left <= right:
            mid = (left + right) // 2
            idx = search(mid)
            if idx != -1:
                start = idx
                max_len = mid
                left = mid + 1
            else:
                right = mid - 1

        return "" if start == -1 else s[start:start + max_len]