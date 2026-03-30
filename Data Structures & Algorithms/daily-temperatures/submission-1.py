class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res =[0]*n
        stack =[]  # stores [temp, index]
        for i, t in enumerate(temperatures):
            while stack and t>stack[-1][0]:
                stackT, stackindex = stack.pop()  
                res[stackindex] = i-stackindex
            stack.append((t, i))  

        return res
            
                    

        