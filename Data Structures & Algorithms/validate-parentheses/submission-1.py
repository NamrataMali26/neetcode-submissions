class Solution:
    def isValid(self, s: str) -> bool:
        mp = {"]": "[", ")": "(", "}": "{"}
        stack = []
        for st in s: 
            if st in mp:
                if stack and stack[-1]==mp[st]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(st)

    
        return True if not stack else False
        