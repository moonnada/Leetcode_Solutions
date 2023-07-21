class Solution:
    def countBits(self, n: int) -> List[int]:
        '''
        U:
        
        P:
            1. init an ans list
            2. iterative until n+1 to convert binary numbers
        '''
        
        def count(x):
            cnt = 0
            while x != 0:
                x &= x-1
                cnt += 1
            
            return cnt
        
        ans = [0] * (n+1)
        
        for x in range(n+1):
            ans[x] = count(x)
            
        return ans