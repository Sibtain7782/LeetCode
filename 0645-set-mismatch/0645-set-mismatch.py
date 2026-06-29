class Solution:
    def findErrorNums(self, nums):
        seen = set()
        duplicate = -1
        missing = -1

        # Find the duplicate number
        for num in nums:
            if num in seen:
                duplicate = num
            else:
                seen.add(num)

        # Find the missing number
        for i in range(1, len(nums) + 1):
            if i not in seen:
                missing = i
                break

        return [duplicate, missing]