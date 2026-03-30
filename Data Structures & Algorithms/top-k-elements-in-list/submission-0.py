class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp={}
        for n in nums:
            if n in mp:
                mp[n] = mp.get(n, 0) +1
            else:
                mp[n]=1

        sorted_dict = list(sorted(mp.items(), key = lambda x:x[1], reverse = True))[:k]

        dict2 = dict(sorted_dict)
        return list(dict2.keys())