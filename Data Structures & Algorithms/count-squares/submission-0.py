from collections import defaultdict
class CountSquares:

    def __init__(self):
        self.pointsMap = defaultdict(int)
        self.points = []

    def add(self, point: List[int]) -> None:
        self.points.append(point)
        self.pointsMap[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for x, y in self.points:
            if abs(px - x) != abs(py - y) or (px == x and py == y):
                continue
            res += self.pointsMap[(x, py)] * self.pointsMap[(px, y)]
        return res            
