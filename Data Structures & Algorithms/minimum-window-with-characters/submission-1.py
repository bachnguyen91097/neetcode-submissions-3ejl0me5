'''
Brute force would be to generate
all substrings from s, and compare them
against t

Generate all substring will be O(n^2)
Compare will be O(n)
-> Total will be O(n^3) -> too slow
'''
from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # safety check, though the constraint here implies that we don't need this check
        if not s or not t:
            return ""

        target = Counter(t)          # frequency map of t
        window = defaultdict(int)    # current window counts

        required = len(target)       # number of unique chars needed
        formed = 0                   # how many are satisfied

        left = 0
        best_len = float("inf")        # because we are looking of the shortest answer
        best = (0, 0)

        for right in range(len(s)):
            char = s[right]
            window[char] += 1

            # ✅ TODO 1:
            # If this char is in target AND its count just matched target count
            # then increase formed
            if char in target and target[char] == window[char]:
                formed += 1

            # Try to SHRINK window
            while formed == required:
                # ✅ TODO 2:
                # Update best window if current is smaller
                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best = (left, right)
                # or 
                # best_len = min(best_len, right - left + 1)

                left_char = s[left]
                window[left_char] -= 1

                # ✅ TODO 3:
                # If left_char is in target AND its count fell below required
                # then decrease formed
                if left_char in target and window[left_char] < target[left_char]:
                    formed -= 1

                left += 1

        # ✅ TODO 4:
        # Return the substring using best indices
        # If no valid window found, return ""
        left, right = best
        return s[left: right + 1] if best_len != float("inf") else ""


            