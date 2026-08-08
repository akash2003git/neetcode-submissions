class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for s in tokens:
            if s in "+-*/":
                b = stack.pop()
                a = stack.pop()
                
                match s:
                    case "+":
                        res = a + b
                    case "-":
                        res = a - b
                    case "*":
                        res = a * b
                    case "/":
                        res = int(a / b)
                
                stack.append(res)
            else:
                stack.append(int(s))
        
        return stack[0]