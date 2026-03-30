class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums) 
        # if len(nums)==0:
        #     return 0
        max_len = 0
        for n in numSet:
            if (n-1) not in numSet:
                curr_len = 1
                while (n+curr_len) in numSet:
                    curr_len+=1
                max_len = max(max_len, curr_len)

        # curr_len=1
        # for i in range(1, len(sorted_nums)): 
        #     if sorted_nums[i]-sorted_nums[i-1]==1:
        #         curr_len = curr_len+1
        #         max_len = max(max_len, curr_len)
        #     else:
        #         curr_len =1
        return max_len

            

