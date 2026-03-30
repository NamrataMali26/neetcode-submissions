class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack =[]

        for t in tokens:
            if t=="+":
                res = int(stack.pop()) + int(stack.pop())
                stack.append(res)
            elif t=="-":
                val1 = int(stack.pop())
                val2 = int(stack.pop())
                res = val2 -val1
                stack.append(res)
            elif t=="*":
                res = int(stack.pop()) * int(stack.pop())
                stack.append(res)
            elif t=="/":
                val1 = int(stack.pop())
                val2 = int(stack.pop())
                res = int(val2/val1)
                stack.append(res)
            else:
                stack.append(int(t))
        return stack[0]
        