class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda x:x[0])
        # intervals.sort(key=lambda x:x[0])
        res =[intervals[0]] #[1,3]
        for i in range(1, len(intervals)):
            # start of curr interval < end of prev in res 
            prev_start, prev_end = res[-1][0], res[-1][1] ##1, 5
            curr_start, curr_end = intervals[i][0], intervals[i][1] #6, 7
            if curr_start <= prev_end:
                res[-1][1] = max(curr_end, prev_end) ##[1, 5]
            else:
                res.append(intervals[i]) 
        return res



        