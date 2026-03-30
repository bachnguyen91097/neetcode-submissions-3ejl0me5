class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        stack = [root]
        visited = [False]
        res = []

        while stack:
            curr, is_visited = stack.pop(), visited.pop()
            if curr:
                if is_visited:
                    res.append(curr.val)
                else:
                    stack.append(curr)
                    visited.append(True)
                    stack.append(curr.right)
                    visited.append(False)
                    stack.append(curr.left)
                    visited.append(False)
        return res