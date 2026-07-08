class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        queue = deque()
        maxHeap = []
        tasks_counter = Counter(tasks)
        for task in tasks_counter:
            heapq.heappush(maxHeap, (-1 * tasks_counter[task], task))

        current_time = 0
        while maxHeap or queue:
            current_time += 1

            if maxHeap:
                task_count, task = heapq.heappop(maxHeap)
                if -1 * task_count > 1:
                    queue.append((task, -1 * task_count, current_time + n))
            
            if queue and queue[0][2] == current_time:
                next_task, next_task_count, task_time = queue.popleft()
                heapq.heappush(maxHeap, (-1 * (next_task_count - 1), next_task))
        return current_time