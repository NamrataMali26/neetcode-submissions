class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s==s[::-1]:
            return True
        for i in range(len(s)):
            new_str = s[:i] + s[i+1:]
            if new_str == new_str[::-1]:
                return True
        return False
        