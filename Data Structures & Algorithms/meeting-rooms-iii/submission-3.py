class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # map to keep track room and its according number of time used
        room_to_count = [0] * n
        
        # sorted based on start time
        sorted_meetings = sorted(meetings, key=lambda meeting: meeting[0])
        # meetings = [[1,20],[2,10],[3,5],[4,9],[6,8]]

# KEY PARTS ----------------------------------------------------------
        free_rooms = [i for i in range(n)]
        busy_rooms = []

        for meeting in sorted_meetings:
            current_start, current_end = meeting
            duration = current_end - current_start
            while busy_rooms and busy_rooms[0][0] <= current_start:
                end_time, room_number = heapq.heappop(busy_rooms)
                heapq.heappush(free_rooms, room_number)
            
            if free_rooms:
                room_number = heapq.heappop(free_rooms)
                finish_time = current_end
                room_to_count[room_number] += 1
            else:
                earliest_end, room_number = heapq.heappop(busy_rooms)
                finish_time = earliest_end + duration
                room_to_count[room_number] += 1
            
            heapq.heappush(busy_rooms, (finish_time, room_number))
# ----------------------------------------------------------------------
        
        return room_to_count.index(max(room_to_count))



