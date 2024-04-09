class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        
        dic = {}
        
        for val in s:
            if val in dic:
                dic[val] += 1
            else:
                dic[val] = 1
                
        for val in t:
            if val not in dic or dic[val] == 0:
                return False
            
            dic[val] -= 1
            
        return True