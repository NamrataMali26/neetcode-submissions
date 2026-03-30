class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l , r=1, max(piles)
        res = r
        while l <= r: 
            k = (l+r)//2
            total_hrs =0 
            for pile in piles:
                hr = math.ceil(pile/k)
                total_hrs += hr
            if total_hrs <= h: 
                res=k
                r=k-1
            else:
                l = k+1
        return res



        