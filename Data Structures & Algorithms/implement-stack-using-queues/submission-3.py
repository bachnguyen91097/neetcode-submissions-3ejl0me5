class MyStack:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        n = len(self.queue)
        while n > 1:
            popped = self.queue.pop(0)
            self.queue.append(popped)
            n -= 1
        return self.queue.pop(0)

    def top(self) -> int:
        n = len(self.queue)
        while n > 1:
            popped = self.queue.pop(0)
            self.queue.append(popped)
            n -= 1
        top = self.queue.pop(0)
        self.queue.append(top)
        return top

    def empty(self) -> bool:
        return len(self.queue) == 0