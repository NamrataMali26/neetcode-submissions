class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res= 0
       
        for i in range(len(s)):
            count, maxFreq = {}, 0
            for j in range(i, len(s)):
                count[s[j]] = 1+ count.get(s[j], 0)
                maxFreq = max(maxFreq, count[s[j]])
                if (j-i+1) -maxFreq <= k:
                    res = max(res, j-i+1)
        return res        