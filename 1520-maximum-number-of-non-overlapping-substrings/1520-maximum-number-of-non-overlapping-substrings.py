class Solution:
    def maxNumOfSubstrings(self, s: str):
        n = len(s)

        # First and last occurrence of every character
        first = [n] * 26
        last = [-1] * 26

        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            first[idx] = min(first[idx], i)
            last[idx] = i

        # Find all valid minimal intervals
        intervals = []

        for c in range(26):
            if first[c] == n:
                continue

            l = first[c]
            r = last[c]
            i = l
            valid = True

            while i <= r:
                idx = ord(s[i]) - ord('a')

                # This character appeared before l,
                # so the substring cannot contain all its occurrences.
                if first[idx] < l:
                    valid = False
                    break

                r = max(r, last[idx])
                i += 1

            if valid:
                intervals.append((l, r))

        # Choose maximum number of non-overlapping intervals.
        # Sorting by ending position also gives minimum total length
        # among solutions with maximum count.
        intervals.sort(key=lambda x: x[1])

        ans = []
        end = -1

        for l, r in intervals:
            if l > end:
                ans.append(s[l:r + 1])
                end = r

        return ans