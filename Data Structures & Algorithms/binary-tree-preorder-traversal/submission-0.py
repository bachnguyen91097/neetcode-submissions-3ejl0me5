class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = [root.val]
        if root.left:
            res.extend(self.preorderTraversal(root.left))
        if root.right:
            res.extend(self.preorderTraversal(root.right))
        return res