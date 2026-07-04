class FileSystem:

    def __init__(self):
        self.paths = set()
        self.path_to_value = {}

    def createPath(self, path: str, value: int) -> bool:
        if path in self.path_to_value:
            return False
        path_list = path.split('/')[1:-1]
        old_path = "/" + "/".join(path_list)
        if old_path != "/" and old_path not in self.path_to_value:
            return False
        self.path_to_value[path] = value
        return True    

    def get(self, path: str) -> int:
        return self.path_to_value.get(path, -1)


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
