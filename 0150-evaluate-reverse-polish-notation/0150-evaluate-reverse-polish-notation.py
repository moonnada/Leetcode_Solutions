class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i not in "+-*/":
                stack.append(int(i))
                continue
            
         
            
            num2 = stack.pop()
            num1 = stack.pop()
            
            if i == "+":
                newVal = num1 + num2
            if i == "-":
                newVal = num1 - num2
            if i == "*":
                newVal = num1 * num2
            if i == "/":
                newVal = int(num1 / num2)
                    
            stack.append(newVal)
                    
        return stack.pop()
                        
        