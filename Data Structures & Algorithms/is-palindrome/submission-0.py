class Solution:
    def isPalindrome(self, s: str) -> bool:
        res=[]
        for word in s:
            if word.isalnum():
                res.append(list(word.lower()))
        print(res)
        print(res[::-1])
        return res==res[::-1]
        