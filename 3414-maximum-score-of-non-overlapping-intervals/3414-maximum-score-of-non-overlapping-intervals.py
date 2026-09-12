from bisect import bisect_right

class Solution:
    def maximumWeight(self, intervals):
        n = len(intervals)

        # Store: [left, right, weight, original_index]
        arr = []
        for i, (l, r, w) in enumerate(intervals):
            arr.append((l, r, w, i))

        # Sort by ending position
        arr.sort(key=lambda x: x[1])

        ends = [x[1] for x in arr]

        # prev[i] = last interval that ends BEFORE arr[i] starts
        prev = []
        for i in range(n):
            l = arr[i][0]

            # Strictly less than l because touching boundaries overlap
            j = bisect_right(ends, l - 1) - 1
            prev.append(j)

        # dp[k][i] = best result using first i intervals with at most k intervals
        # Store (score, tuple of indices)
        dp = [[(0, ()) for _ in range(n + 1)] for _ in range(5)]

        for k in range(1, 5):
            for i in range(1, n + 1):
                # Don't take current interval
                best = dp[k][i - 1]

                # Take current interval
                idx = i - 1
                l, r, w, original_idx = arr[idx]

                p = prev[idx] + 1

                old_score, old_indices = dp[k - 1][p]

                candidate = (
                    old_score + w,
                    tuple(sorted(old_indices + (original_idx,)))
                )

                # Maximum score first
                # If scores equal, lexicographically smallest indices
                if candidate[0] > best[0]:
                    best = candidate
                elif candidate[0] == best[0] and candidate[1] < best[1]:
                    best = candidate

                dp[k][i] = best

        return list(dp[4][n][1])