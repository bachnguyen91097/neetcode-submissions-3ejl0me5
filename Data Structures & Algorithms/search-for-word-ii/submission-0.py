class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board, words):
        rows, cols = len(board), len(board[0])
        root = TrieNode()

        # build trie
        for w in words:
            node = root
            for ch in w:
                node = node.children.setdefault(ch, TrieNode())
            node.word = w

        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        res = []

        def dfs(r, c, node):
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return

            char = board[r][c]
            if char not in node.children:
                return

            next_node = node.children[char]

            if next_node.word:
                res.append(next_node.word)
                next_node.word = None  # avoid duplicates

            board[r][c] = "#"

            for dr, dc in directions:
                dfs(r + dr, c + dc, next_node)

            board[r][c] = char

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return res