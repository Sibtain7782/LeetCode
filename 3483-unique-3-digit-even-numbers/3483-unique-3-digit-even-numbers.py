class Solution:
    def totalNumbers(self, digits):
        ans = set()
        n = len(digits)

        for i in range(n):
            for j in range(n):
                for k in range(n):

                    # Same digit copy ko dobara use nahi karna
                    if i == j or j == k or i == k:
                        continue

                    # Leading zero allowed nahi
                    if digits[i] == 0:
                        continue

                    # Last digit even hona chahiye
                    if digits[k] % 2 != 0:
                        continue

                    num = digits[i] * 100 + digits[j] * 10 + digits[k]
                    ans.add(num)

        return len(ans)