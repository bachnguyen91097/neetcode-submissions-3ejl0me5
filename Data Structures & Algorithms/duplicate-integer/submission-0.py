class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hmap = {}
        for num in nums:
            if num in hmap:
                return True
            else:
                hmap[num] = 1
        return False