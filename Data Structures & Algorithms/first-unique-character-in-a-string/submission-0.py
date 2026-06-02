class Solution:
    def firstUniqChar(self, s: str) -> int:
        sCounter = Counter(s)
        uniqChar = ""
        for k in sCounter:
            if sCounter[k] == 1:
                uniqChar = k
                break
        if not uniqChar:
            return -1
        for i in range(len(s)):
            if s[i] == uniqChar:
                return i