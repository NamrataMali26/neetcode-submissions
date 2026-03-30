class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort(key = lambda x:x[0])
        prev_start, prev_end = intervals[0][0], intervals[0][1]

        for i in range(1, len(intervals)):
            curr_start, curr_end = intervals[i][0], intervals[i][1]
            if curr_start < prev_end:
                res+=1
                prev_end = min(curr_end, prev_end)
            else:
                prev_end = curr_end
        return res
