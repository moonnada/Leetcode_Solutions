class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
        given three parameters
        '''
        if len(position) == 1 and len(speed) == 1: return 1
        
        pair = [[p,s] for p,s in zip(position, speed)]
        
        stack = []
        
        for p,s in sorted(pair)[::-1]:
            stack.append((target-p)/s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)