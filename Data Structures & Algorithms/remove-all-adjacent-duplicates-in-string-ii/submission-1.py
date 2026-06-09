class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        counts = []
        for i in range(len(s)):
            if not stack or stack[-1] != s[i]:
                stack.append(s[i])
                counts.append(1)
            else:
                stack.append(s[i])
                counts[-1] += 1
                if counts[-1] == k:
                    for j in range(k):
                        stack.pop()
                    counts.pop()

        return "".join(stack)