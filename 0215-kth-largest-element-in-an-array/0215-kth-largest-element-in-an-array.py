import random

class Solution:
    def findKthLargest(self, nums, k):
        k = len(nums) - k

        def quick_select(left, right):
            pivot = nums[random.randint(left, right)]

            l, r = left, right

            while l <= r:
                while nums[l] < pivot:
                    l += 1
                while nums[r] > pivot:
                    r -= 1

                if l <= r:
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1
                    r -= 1

            if k <= r:
                return quick_select(left, r)
            if k >= l:
                return quick_select(l, right)

            return nums[k]

        return quick_select(0, len(nums) - 1)