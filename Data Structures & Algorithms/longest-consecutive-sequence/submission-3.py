class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_nums = sorted(set(nums)) #-1, 0, 1, 3, 4, 5, 6, 7, 8, 9
        if len(nums)==0:
            return 0
        max_len = 1
        curr_len=1

        for i in range(1, len(sorted_nums)): 
            if sorted_nums[i]-sorted_nums[i-1]==1:
                curr_len = curr_len+1
                max_len = max(max_len, curr_len)
            else:
                curr_len =1
        return max_len

            

