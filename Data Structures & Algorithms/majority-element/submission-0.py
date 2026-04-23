class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mp ={}
        for n in nums:
            if n not in mp:
                mp[n] = 0
            else:
                mp[n] +=1
        sorted_mp = dict(list(sorted(mp.items(), key = lambda x: x[1], reverse = True))[:1])
        return list(sorted_mp.keys())[0]
        