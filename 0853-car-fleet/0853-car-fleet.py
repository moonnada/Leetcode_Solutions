class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
        U:
            q) always both input lists' lengths are same?
            
            ex) p = [10, 8, 0, 5, 3] , s = [2, 4, 1, 1, 3]
            sum = [12, 12, 1, 6,6]
            
        M : stack
        
        P: 
            1. check edge case( one length of list)
            2. traverse the input list to put added val from both lists into set
                2.1) if set not has the added val, put into set
            3. return set's length
        '''
        
        if len(position) == 1 and len(speed) == 1: return 1
        
        pair = [[p,s] for p,s in zip(position, speed)]
        
        stack = []
        
        for p,s in sorted(pair)[::-1]: #reverse sorted order
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
       