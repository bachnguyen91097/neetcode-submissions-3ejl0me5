class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        l, r = 0, 0
        longest_substring_len = 1
        seen = set()

        while r < len(s):
            if s[r] in seen:
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
            seen.add(s[r])
            current_length = r - l + 1
            longest_substring_len = max(longest_substring_len, current_length)
            r += 1
        return longest_substring_len