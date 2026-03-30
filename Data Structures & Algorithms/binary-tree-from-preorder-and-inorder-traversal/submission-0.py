# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hmap = {val: idx for idx,val in enumerate(inorder)}
        pre_idx = 0
        def dfs(l,r):
            nonlocal pre_idx
            if l > r:
                return None
            root_val = preorder[pre_idx]
            pre_idx += 1
            root = TreeNode(root_val)
            root_idx = hmap[root_val]
            root.left = dfs(l, root_idx - 1)
            root.right = dfs(root_idx + 1, r)
            return root
        return dfs(0, len(preorder) - 1)
        