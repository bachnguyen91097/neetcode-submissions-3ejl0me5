# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val
        def helper(node):
            nonlocal res
            if not node:
                return 0
            left_child_value = max(0, helper(node.left))
            right_child_value = max(0, helper(node.right))
            res = max(res, node.val + left_child_value + right_child_value)
            return node.val + max(left_child_value, right_child_value)
        helper(root)
        return res