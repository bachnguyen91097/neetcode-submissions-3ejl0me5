from collections import deque

class Solution:
    def timeTaken(self, arrival: List[int], state: List[int]) -> List[int]:
        enter_queue = deque()
        exit_queue = deque()
        current_time = 0
        ans = [0] * len(arrival)
        door_state = -1 # unused
        i = 0
        while enter_queue or exit_queue or i < len(arrival):
            while i < len(arrival) and arrival[i] <= current_time:
                if state[i] == 0:
                    enter_queue.append(i)
                elif state[i] == 1:
                    exit_queue.append(i)
                i += 1

            if not enter_queue and not exit_queue:
                current_time = arrival[i]
                door_state = -1
                continue
            
            if door_state == -1 or door_state == 1:
                if exit_queue:
                    idx = exit_queue.popleft()
                    ans[idx] = current_time
                    door_state = 1
                elif enter_queue:
                    idx = enter_queue.popleft()
                    ans[idx] = current_time
                    door_state = 0
            elif door_state == 0:
                if enter_queue:
                    idx = enter_queue.popleft()
                    ans[idx] = current_time
                    door_state = 0
                elif exit_queue:
                    idx = exit_queue.popleft()
                    ans[idx] = current_time
                    door_state = 1
            current_time += 1
        
        return ans