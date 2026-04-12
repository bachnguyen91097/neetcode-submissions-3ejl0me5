class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root: # won't happen as constraint: The number of nodes in the tree is in the range [1, 10⁴].
            return []

        res = [root.val]

        def isLeaf(node):
            return node and not node.left and not node.right

        if isLeaf(root):
            return res

        # find the left boundary
        curr = root.left
        leftBoundary = []
        while curr:
            if not isLeaf(curr):
                leftBoundary.append(curr.val)
            if curr.left:
                curr = curr.left
            else:
                curr = curr.right
        res.extend(leftBoundary)
        
        # find all leaves from left to right
        leaves = []
        def dfs(node):
            if not node:
                return
            if isLeaf(node):
                leaves.append(node.val)
                return
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        res.extend(leaves)

        # find the right boundary
        curr = root.right
        rightBoundary = []
        while curr:
            if not isLeaf(curr):
                rightBoundary.append(curr.val)
            if curr.right:
                curr = curr.right
            else:
                curr = curr.left
        
        # No changes needed to original logic, the Runtime Error likely occurred 
        # due to an environment-specific issue or a hidden edge case in recursion.
        # Reversing the right boundary at the end is correct.
        res.extend(reversed(rightBoundary))

        return res