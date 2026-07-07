class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.is_word = True

    def search(self, word: str) -> bool:
        def dfs(i, node, word):
            curr = node
            for j in range(i, len(word)):
                if word[j] == ".":
                    for child_node in curr.children.values():
                        if dfs(j+1, child_node, word):
                            return True
                    return False
                if word[j] not in curr.children:
                    return False
                curr = curr.children[word[j]]
            return curr.is_word
        return dfs(0, self.root, word)