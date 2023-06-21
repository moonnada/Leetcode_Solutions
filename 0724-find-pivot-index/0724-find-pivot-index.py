class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        '''
        U:
        ex) nums = [1, 7, 3, 6, 5, 6]
            totalsum = 28
            leftsum = 0
        M: prefix
           
        P:
            0. check edge cases(empty, one element)
            1. get totalSum
            2. init a leftSum as 0
            3. traverse the input list to find a pivot
                3.1) get a rightSum. rightSum = totalSum - leftSum - curIndex
                3.2) if leftSum == rightSum, return curIndex
                3.3) else curElement is added to the leftSum
            4. return -1
           
        '''
        
        totalSum = sum(nums)
        leftSum = 0
        for i in range(len(nums)):
            rightSum = totalSum - leftSum - nums[i]
            if leftSum == rightSum: return i
            else: leftSum += nums[i]
                
        return -1
        
        
     