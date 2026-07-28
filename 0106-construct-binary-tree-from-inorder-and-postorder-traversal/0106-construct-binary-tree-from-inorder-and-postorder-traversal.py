class Solution:
    def buildTree(self, inorder, postorder):
        inorder_map = {value: i for i, value in enumerate(inorder)}

        def helper(left, right):
            if left > right:
                return None

            root_val = postorder.pop()
            root = TreeNode(root_val)

            index = inorder_map[root_val]

            root.right = helper(index + 1, right)
            root.left = helper(left, index - 1)

            return root

        return helper(0, len(inorder) - 1)