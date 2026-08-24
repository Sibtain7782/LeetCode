class Solution:
    def sortedListToBST(self, head):
        # Convert linked list to array
        nums = []

        while head:
            nums.append(head.val)
            head = head.next

        # Build BST from sorted array
        def build(left, right):
            if left > right:
                return None

            mid = (left + right) // 2

            root = TreeNode(nums[mid])

            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(nums) - 1)