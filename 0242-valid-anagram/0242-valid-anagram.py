class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        
        d = {}
        
        for val in s:
            if val in d:
                d[val] += 1
            else:
                d[val] = 1
                
        for val in t:
            if not val in d or d[val] == 0: return False
            
            d[val] -= 1
            
        return True