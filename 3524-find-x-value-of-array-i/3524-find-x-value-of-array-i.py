class Solution:
    def resultArray(self, nums, k):
        dp = [0] * k
        ans = [0] * k

        for num in nums:
            val = num % k
            new_dp = [0] * k

            # Start a new subarray with nums[i]
            new_dp[val] += 1

            # Extend previous subarrays
            for r in range(k):
                if dp[r]:
                    new_r = (r * val) % k
                    new_dp[new_r] += dp[r]

            # Add subarrays ending at this position
            for r in range(k):
                ans[r] += new_dp[r]

            dp = new_dp

        return ans