class Solution:
    def timeTaken(self, arrival: List[int], state: List[int]) -> List[int]:
        enter_queue = deque()
        exit_queue = deque()
        door_state = -1 # not used, 0 is enter, 1 is exit
        current_time = 0
        answer = [0] * len(arrival)
        
        i = 0
        while i < len(arrival) or exit_queue or enter_queue:
            # Add all people who have arrived by current_time to their respective queues
            while i < len(arrival) and arrival[i] <= current_time:
                if state[i] == 0:
                    enter_queue.append(i)
                else:
                    exit_queue.append(i)
                i += 1
            
            # If no one is waiting, skip time to next arrival and reset door
            if not enter_queue and not exit_queue:
                current_time = arrival[i]
                door_state = -1
                continue
            
            if door_state == -1 or door_state == 1:
                if exit_queue:
                    idx = exit_queue.popleft()
                    answer[idx] = current_time
                    door_state = 1
                else:
                    idx = enter_queue.popleft()
                    answer[idx] = current_time
                    door_state = 0
            elif door_state == 0:
                if enter_queue:
                    idx = enter_queue.popleft()
                    answer[idx] = current_time
                    door_state = 0
                else:
                    idx = exit_queue.popleft()
                    answer[idx] = current_time
                    door_state = 1
            current_time += 1
        return answer
