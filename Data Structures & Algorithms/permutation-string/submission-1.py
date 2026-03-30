class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        if s1 == s2:
            return True
        
        dict_s1 = Counter(s1)
        window_length = len(s1)
        l, r = 0, window_length - 1
        curr = s2[l: r+1]
        counter_curr = Counter(curr)
        while r < len(s2):
            if counter_curr == dict_s1:
                return True
            else:
                counter_curr[s2[l]]-= 1
                if counter_curr[s2[l]] == 0:
                    del counter_curr[s2[l]]
                l += 1
                r += 1
                if r < len(s2):
                    counter_curr[s2[r]] += 1
        return False