class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        n = len(text)
        seen = set()

        for i in range(n):
            for length in range(1, (n - i) // 2 + 1):

                first = text[i:i + length]
                second = text[i + length:i + 2 * length]

                if first == second:
                    seen.add(first + second)

        return len(seen)