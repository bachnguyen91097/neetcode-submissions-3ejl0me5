class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        s_counter = Counter(s)
        l = 0
        current_set = set()
        for r in range(len(s)):
            current_char = s[r]
            current_set.add(current_char)
            s_counter[current_char] -= 1
            if s_counter[current_char] == 0:
                current_set.remove(current_char)
            if not current_set:
                res.append(r - l + 1)
                l = r + 1
        return res