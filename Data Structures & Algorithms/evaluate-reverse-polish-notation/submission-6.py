class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack =[]

        for t in tokens:
            if t=="+":
                res = stack.pop() + stack.pop()
                stack.append(res)
            elif t=="-":
                val1 = stack.pop()
                val2 = stack.pop()
                res = val2 -val1
                stack.append(res)
            elif t=="*":
                res = stack.pop() * stack.pop()
                stack.append(res)
            elif t=="/":
                val1 = float(stack.pop())
                val2 = float(stack.pop())
                res = int(val2/val1)
                stack.append(res)
            else:
                stack.append(int(t))
        return stack[0]
        