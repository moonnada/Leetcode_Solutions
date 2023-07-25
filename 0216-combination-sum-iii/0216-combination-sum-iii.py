class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        def backtrack(start, target, k, res):
            if k == 0 and target == 0:
                return [[]]
            if k == 0 and target < 0:
                return []
            
            ans = []
            
            for i in range(start, 10):
                for combo in backtrack(i+1, target - i, k-1, res):
                    ans.append([i] + combo)
            return ans
        
        return backtrack(1,n,k,[])