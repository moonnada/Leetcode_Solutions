class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        '''
        U:
            key points: 
                1. all numbers in the input list are distinct
                2. if the target is found the list, return the index. if not, return the index where it should be
                
        M: binary
        
        P:
            1. init left and right ptrs
            2. while left <= right,
                2.1) get pivot point
                2.2) if target and pivots element is equal, return the pivot
                2.3) if target > pivots element, left++
                2.4) if target < pivots element, right++
            3. return left
        
        time: o(lgn), space: o(1)
        '''
        
        left = 0
        right = len(nums)-1
        
        while left <= right:
            pivot = (left+right) // 2
            if nums[pivot] == target: return pivot
            
            if nums[pivot] < target: left+=1
            
            if nums[pivot] > target: right-=1
                
        return left