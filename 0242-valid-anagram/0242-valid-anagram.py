class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = defaultdict(int)
        for i in s:
            count[i] += 1
            
        for i in t:
            count[i] -= 1
            
        for val in count.values():
            if val != 0: return False
        
        return True
        
#         1. init a hashmap to put the 's' input
#         2. traverse the 't' str to find anagram
#           2.1) if hashmap has the cur element, reduce the cnt
#            2.2) else return false
#          3. if map not have any element, return true else false


    
        
        