class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        order_dict = {c: set() for w in words for c in w}
        indegree = {c: 0 for c in order_dict}
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i+1]
            n = min(len(word1), len(word2))
            if len(word1) > len(word2) and word1[:n] == word2[:n]:
                return ""
            for j in range(n):
                if word1[j] == word2[j]:
                    continue
                else:
                    if word2[j] not in order_dict[word1[j]]:
                        order_dict[word1[j]].add(word2[j])
                        indegree[word2[j]] += 1
                    break
        # Now it becomes topology sort problem

        q = deque([c for c in indegree if indegree[c] == 0]) 
        res = []

        while q:
            char = q.popleft()
            res.append(char)
            for neighbor in order_dict[char]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        if len(res) != len(indegree):
            return ""
        return "".join(res)       