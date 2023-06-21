class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        '''
        U:
            q) are input lists sorted?
            
            ex) [1,2,3]  ,  [2,4,6]
            =>  [ [1,3], [4,6]]
            
        M: set
        
        P: 
            1. init two sets for each list 
            2. return as a list with comparing the two sets
        '''
        
        set1 = set(nums1)
        set2 = set(nums2)
        
        return [list(set1-set2), list(set2-set1)]