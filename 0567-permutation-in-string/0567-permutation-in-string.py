class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        
        cntS1, cntS2 = [0]*26, [0]*26
        for i in range(len(s1)):
            cntS1[ord(s1[i]) - ord('a')] += 1
            cntS2[ord(s2[i]) - ord('a')] += 1
            
        if cntS1 == cntS2: return True
        
        for right in range(len(s1), len(s2)):
            cntS2[ord(s2[right]) - ord('a')] += 1
            cntS2[ord(s2[right - len(s1)]) - ord('a')] -= 1
            
            if cntS1 == cntS2: return True
        return False
        
#         Time : o(n), space : o(n)
#         s1d = {}
#         s2d = {}
#         left = 0
        
#         if len(s1) > len(s2): return False
        
#         for char in s1:
#             s1d[char] = s1d.get(char,0)+1
            
#         for i in range(len(s1)):
#             s2d[s2[i]] = s2d.get(s2[i],0) + 1
            
#         if s1d == s2d:
#             return True
        
#         for right in range(len(s1), len(s2)):
#             s2d[s2[right]] = s2d.get(s2[right], 0 ) + 1
            
#             s2d[s2[left]] -= 1
#             if s2d[s2[left]] == 0:
#                 del s2d[s2[left]]
#             left += 1
            
#             if s1d == s2d: return True
            
#         return False
    
    
        
            
            
                