class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
# #       0. check edge case  
#         1. init a dict
#         2. traverse to put the 's' element into the dict
#         3. traverse to decrement the 't'element in the dict
#         4. iterative the dict to compare dicts value
        

#         if len(s) != len(t): return False
        
#         count = defaultdict(int)
        
#         for i in s:
#             count[i] += 1
            
#         for i in t:
#             count[i] -= 1
            
#         for val in count.values():
#             if val != 0:
#                 return False

        count = {}
        
        for i in s:
            count[i] = count.get(i,0) + 1
            
        for i in t:
            count[i] = count.get(i,0 )-1
            
        for i in count.values():
            if i != 0: return False
            
    
            
        return True
            
#         count = defaultdict(int)
#         for i in s:
#             count[i] += 1
            
#         for i in t:
#             count[i] -= 1
            
#         for val in count.values():
#             if val != 0: return False
        
#         return True


        

    

    
        
        