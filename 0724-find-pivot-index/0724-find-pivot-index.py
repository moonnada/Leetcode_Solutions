class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        '''
        U:
        nums = [1, 7, 3, 6, 5, 6]
      leftSum : 1  8  11 17 22 28
      rightSum :28   27    20  17  11  6
               
           
           
        P:
        
            - init two ptrs(left and right)
            - while left < right
                - leftSum += curLeft, left++
                - rightSum += curRight, right--
                
                if leftSum == rightSum
        '''
        S = sum(nums)
        leftsum = 0
        for i, x in enumerate(nums):
            if leftsum == (S - leftsum - x):
                return i
            leftsum += x
        return -1
        