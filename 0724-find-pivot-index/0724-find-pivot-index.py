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
        totalSum = sum(nums)
        leftSum = 0
        
        for i in range(len(nums)):
            rightSum = totalSum - nums[i] - leftSum
            if leftSum == rightSum: return i
            else: leftSum += nums[i]
        return -1
        