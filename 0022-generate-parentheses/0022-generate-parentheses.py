class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
        Input: n = 3
        Output: ["((()))","(()())","(())()","()(())","()()()"]
        
        only add open brackets if open < n
        only add a closing bracked if closed < open
        valid if open == closed == n
        
        '''
        stack = []
        ans = []
        
        def backtrack(openN, closedN):
            if openN == closedN == n:
                ans.append("".join(stack))
                return
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
                
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN+1)
                stack.pop()
                
        backtrack(0,0)
        return ans