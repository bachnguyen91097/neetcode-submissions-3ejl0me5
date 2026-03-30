class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]
        for i in range(len(nums)):
            nextPerms = []
            for p in perms:
                for j in range(len(p) + 1):
                    if j > 0 and p[j-1] == nums[i]:
                        break
                    pCopy = p.copy()
                    pCopy.insert(j,nums[i])
                    nextPerms.append(pCopy)
            perms = nextPerms
        return perms