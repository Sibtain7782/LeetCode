# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.count = 0
        
        def dfs(node):
            if not node:
                return (0, 0)  # (sum, count)
            
            # Get sum and count from left and right subtrees
            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)
            
            # Calculate current subtree sum and count
            current_sum = left_sum + right_sum + node.val
            current_count = left_count + right_count + 1
            
            # Check if the node's value equals the floor average of its subtree
            if node.val == current_sum // current_count:
                self.count += 1
                
            return (current_sum, current_count)
        
        dfs(root)
        return self.count