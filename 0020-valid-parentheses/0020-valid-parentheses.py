class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            match i:
                case '(':
                    stack.append(')')
                case '{':
                    stack.append('}')
                case '[':
                    stack.append(']')
                case default:
                    if not stack or stack.pop() != i: return False
                    
        return len(stack) == 0