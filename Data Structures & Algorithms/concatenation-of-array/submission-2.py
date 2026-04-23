class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = nums.copy()
        res.extend(nums)
        return res
        