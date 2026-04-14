class Element:
    def __init__(self, name):
        self.name = name
        self.isFile = False
        self.content = ""
        self.children = {} # name -> Element

class FileSystem:

    def __init__(self):
        self.root = Element("")
    # This function is to traverse node from root to desired dir/file and create missing
    # dir along the way if needed
    def traverse(self, path):
        curr = self.root
        if path == "/":
            return curr
        for part in path.split("/"):
            if part == "":
                continue
            if part not in curr.children:
                curr.children[part] = Element(part)
            curr = curr.children[part]
        return curr

    def ls(self, path: str) -> List[str]:
        node = self.traverse(path)
        if node.isFile:
            return [node.name]
        return sorted(node.children.keys())

    def mkdir(self, path: str) -> None:
        node = self.traverse(path)

    def addContentToFile(self, filePath: str, content: str) -> None:
        node = self.traverse(filePath)
        node.isFile = True
        node.content += content

    def readContentFromFile(self, filePath: str) -> str:
        return self.traverse(filePath).content


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
