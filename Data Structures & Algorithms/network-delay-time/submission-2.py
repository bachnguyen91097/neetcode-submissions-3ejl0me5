class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u,v,t in times:
            adj[u].append([v,t])
        min_time = {}
        minHeap = [[0, k]]

        while minHeap:
            t, s = heapq.heappop(minHeap)
            if s in min_time:
                continue
            min_time[s] = t
            for s_n, t_n in adj[s]:
                if s_n not in min_time:
                    heapq.heappush(minHeap, [t_n + t, s_n])
        if len(min_time) != n:
            return -1
        return max(min_time.values())