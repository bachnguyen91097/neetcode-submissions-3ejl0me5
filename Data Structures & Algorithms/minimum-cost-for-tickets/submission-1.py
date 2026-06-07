class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = {}

        def helper(i, current_day):
            if i >= len(days):
                return 0
            if current_day >= days[i]:
                return helper(i + 1, current_day)
            if (i, current_day) in dp:
                return dp[(i, current_day)]
            
            first_pass_option = costs[0] + helper(i + 1, days[i])
            second_pass_option = costs[1] + helper(i + 1, days[i] + 6)
            third_pass_option = costs[2] + helper(i + 1, days[i] + 29)
            
            res = min(first_pass_option, second_pass_option, third_pass_option)
            dp[(i, current_day)] = res
            return dp[(i, current_day)]
        return helper(0, 0)