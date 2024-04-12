class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        
        cntS1 , cntS2 = [0]*26, [0]*26
        for i in range(len(s1)):
            cntS1[ord(s1[i]) - ord('a')] += 1
            cntS2[ord(s2[i]) - ord('a')] += 1
            
        if cntS1 == cntS2: return True
        
        for right in range(len(s1), len(s2)):
            cntS2[ord(s2[right]) - ord('a')] += 1
            cntS2[ord(s2[right- len(s1)]) - ord('a')] -= 1
            
            if cntS1 == cntS2: return True
            
        return False
            