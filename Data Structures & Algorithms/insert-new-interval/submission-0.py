class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res =[]
        new_start, new_end = newInterval[0], newInterval[1]
        for i in range(len(intervals)):
            curr_start, curr_end = intervals[i][0], intervals[i][1] 
            
            if new_end < curr_start: 
                res.append([new_start, new_end])
                return res + intervals[i:]
            elif new_start > curr_end:
                res.append([curr_start, curr_end])
            else: 
                new_start = min(new_start, curr_start)
                new_end = max(new_end, curr_end)
        res.append([new_start, new_end])
        return res


