class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        seen = defaultdict(int)
        n = len(s)
        l = 0
        res = float("-inf")

        for r in range(n):
            seen[s[r]] += 1
            while len(seen) > k:
                seen[s[l]] -= 1
                if seen[s[l]] == 0:
                    del seen[s[l]]
                l += 1
            res = max(res, r - l + 1)
        return res