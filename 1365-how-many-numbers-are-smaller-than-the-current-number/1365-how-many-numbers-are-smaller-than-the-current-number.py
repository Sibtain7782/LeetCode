class Solution:
    def smallerNumbersThanCurrent(self, nums):
        sorted_nums = sorted(nums)
        rank = {}

        # Store the first index of each number
        for i, num in enumerate(sorted_nums):
            if num not in rank:
                rank[num] = i

        # Build the answer
        return [rank[num] for num in nums]