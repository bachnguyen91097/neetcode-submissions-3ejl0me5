class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        res = 0
        hmap = defaultdict(int)
        for task in tasks:
            hmap[task] += 1
        maxHeap = []
        for task in hmap:
            heapq.heappush(maxHeap, (-hmap[task]))
        queue = deque()
        while maxHeap or queue:
            res += 1
            if not maxHeap:
                res = queue[0][0]
            else:
                numTask = heapq.heappop(maxHeap)
                newNumTask = numTask * (-1) - 1
                if newNumTask > 0:
                    queue.append([res + n, newNumTask])
            if queue and queue[0][0] == res:
                item = queue.popleft()
                heapq.heappush(maxHeap, (-item[1]))
        return res