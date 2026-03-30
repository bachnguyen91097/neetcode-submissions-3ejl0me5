class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]
        for i in range(len(nums)):
            nextPerms = set()
            for p in perms:
                for j in range(len(p) + 1):
                    pCopy = p.copy()
                    pCopy.insert(j,nums[i])
                    nextPerms.add(tuple(pCopy))
            perms = list(map(list, nextPerms))
        return perms