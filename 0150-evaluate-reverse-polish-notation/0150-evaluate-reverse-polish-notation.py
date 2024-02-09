class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        '''
        Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
        Output: 22
        
        
        
        if cur char is num, put into stack
        else // cur char is an operator
            val2 = stack.pop
            val1 = stack.pop
            
            newVal = val1, cur operater, val2
            stack.append(newVal)
        '''
        
        stack = []
        val1 = val2 = ""
        for i in tokens:
            if i not in "+-*/":
                stack.append(int(i))
                continue
                
            val2 = stack.pop()
            val1 = stack.pop()    
            
            if i == "+":
                newVal = val1 + val2
            elif i == "-":
                newVal = val1 - val2
            elif i == "*":
                newVal = val1 * val2
            elif i == "/":
                newVal = int(val1 / val2)
                
            stack.append(newVal)
                
        return stack.pop()