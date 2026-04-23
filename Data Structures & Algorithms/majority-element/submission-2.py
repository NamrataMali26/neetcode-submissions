class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mp ={}
        res = maxCount = 0
        for n in nums:
            if n not in mp:
                mp[n] = 1
            else:
                mp[n] +=1
            if mp[n] > maxCount:
                res = n
                maxCount = mp[n]
    
        return res
        