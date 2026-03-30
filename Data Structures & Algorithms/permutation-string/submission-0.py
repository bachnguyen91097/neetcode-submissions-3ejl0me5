class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        if s1 == s2:
            return True
        
        dict_s1 = Counter(s1)
        window_length = len(s1)
        l, r = 0, window_length - 1
        while r < len(s2):
            if s2[l] not in dict_s1:
                l += 1
                r += 1
            else:
                temp = s2[l:r+1]
                temp_counter = Counter(temp)
                if temp_counter == dict_s1:
                    return True
                else:
                    l += 1
                    r += 1
        return False
