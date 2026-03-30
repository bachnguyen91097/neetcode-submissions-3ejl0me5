class Solution:
    def isValid(self, s: str) -> bool:
        s1 = []
        for c in s:
            if len(s1) != 0:
                top_item = s1[-1]
                if (top_item == '[' and c ==']') or (top_item == '(' and c ==')') or (top_item == '{' and c =='}'):
                    s1.pop()
                else:
                    s1.append(c)
            else:
                s1.append(c)
        return len(s1) == 0