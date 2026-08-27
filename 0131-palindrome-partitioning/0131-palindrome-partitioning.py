class Solution:
    def partition(self, s: str):
        result = []
        path = []

        def isPalindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def backtrack(start):
            # String completely partition ho gayi
            if start == len(s):
                result.append(path[:])
                return

            # Different substrings try karo
            for end in range(start, len(s)):
                
                # Sirf palindrome substring choose karo
                if isPalindrome(start, end):
                    path.append(s[start:end + 1])

                    # Remaining string ke liye recursion
                    backtrack(end + 1)

                    # Backtrack
                    path.pop()

        backtrack(0)
        return result