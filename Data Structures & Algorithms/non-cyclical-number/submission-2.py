class Solution:
    def isHappy(self, n: int) -> bool:
        seen =set()
        while n not in seen:
            seen.add(n)
            n = self.sumofsquares(n)
            if n==1:
                return True
        return False

    def sumofsquares(self, n: int) -> int:
        res =0
        while n:
            res += (n % 10) ** 2
            n = n // 10
        return res
        











        