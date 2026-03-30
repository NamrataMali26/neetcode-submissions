class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # leftProduct =[1]*len(nums)
        # rightProduct =[1]*len(nums)
        res=[1]*len(nums)
        for i in range(1, len(nums)):
            res[i] = res[i-1]*nums[i-1]

        right =1
        for i in range(len(nums)-1, -1, -1):
            res[i] = res[i]*right
            right = right*nums[i]

        # for i in range(len(nums)-2, -1, -1):
        #     rightProduct[i] = rightProduct[i+1]*nums[i+1]
        #     res[i] = rightProduct[i]* leftProduct[i]

        # for i in range(len(nums)):
        #     res[i] = (leftProduct[i]) * (rightProduct[i])
        return res
        




        