class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for i in range(len(nums)):
            if nums[i]>0:
                break
            if nums[i]==nums[i-1] and i>0:
                continue

            l, r = i+1, len(nums)-1
            while l<r:
                threeSum = nums[l]+nums[r]+nums[i]
                if threeSum>0:
                    r-=1
                elif threeSum<0:
                    l+=1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l+=1
                    r-=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
        return res

        