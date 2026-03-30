# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        curr = root
        stack = []
        self.res = []

        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                self.res.append([curr.val, False])
                curr = curr.right        

    def next(self) -> int:
        i = 0
        while i < len(self.res):
            e, visited = self.res[i]
            if not visited:
                self.res[i][1] = True
                print(self.res)
                return e
            i += 1

    def hasNext(self) -> bool:
        i = 0
        while i < len(self.res):
            e, visited = self.res[i]
            if not visited:
                return True
            i += 1
        return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()