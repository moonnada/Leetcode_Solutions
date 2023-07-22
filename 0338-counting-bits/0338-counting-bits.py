class Solution:
    def countBits(self, n: int) -> List[int]:
        '''
        U:
        
        P:
            1. init an ans list
            2. iterative until n+1 to convert binary numbers
        '''
        
        ans = [0] * (n+1)
        for x in range(1, n+1):
            ans[x] = ans[x & (x-1)] + 1
        return ans