class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        '''
        P:
            1. init an ans val 
            2. while one of three input vals exist
                2.1) if the most right val of c is 1, check a and b vals are 1 or not
                2.2) else (the most right val of c is 0), add a and b bits into ans val
                2.3) each val are moved to the right by 1
                
        '''
        ans = 0
        while a or b or c:
            if c & 1:
                ans += 0 if ((a & 1) or (b & 1)) else 1
            else:
                ans += (a & 1) + (b & 1)
                
            a >>= 1
            b >>= 1
            c >>= 1
            
        return ans