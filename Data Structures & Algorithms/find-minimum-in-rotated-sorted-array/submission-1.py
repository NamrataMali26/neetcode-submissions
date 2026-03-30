class Solution:
    def findMin(self, nums: List[int]) -> int:
        l =0
        r =len(nums)-1
       
        while nums[l]>nums[r]:
            r= r-1

        if r<len(nums)-1:
            return nums[r+1]
        else:
            return nums[l]
        