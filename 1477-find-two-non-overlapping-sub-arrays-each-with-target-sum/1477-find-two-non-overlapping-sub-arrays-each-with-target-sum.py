class Solution:
    def minSumOfLengths(self, arr, target):
        n = len(arr)

        # best[i] = minimum length of a valid subarray
        # completely inside arr[0:i]
        best = [float('inf')] * (n + 1)

        left = 0
        curr_sum = 0
        answer = float('inf')

        for right in range(n):
            curr_sum += arr[right]

            # Shrink window if sum is too large
            while curr_sum > target:
                curr_sum -= arr[left]
                left += 1

            # Found a subarray [left, right]
            if curr_sum == target:
                length = right - left + 1

                # Need another valid subarray before 'left'
                if best[left] != float('inf'):
                    answer = min(answer, best[left] + length)

                # Store the shortest valid subarray ending at/before right
                best[right + 1] = min(best[right], length)
            else:
                best[right + 1] = best[right]

        return -1 if answer == float('inf') else answer