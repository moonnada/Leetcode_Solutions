class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        '''
        U:
        q) can input arr be empty?
        q) how many digit of decimal number can I return
        
        M: sliding window
        
        P:
            1. check edge cases(empth, one element)
            2. init curSum and maxSum to the sum of the initial k 
            3. start a loop from the kth element, iterate until reaching the end
                3.1) substart the left element of the window and add the right element of window
                3.2) update the max
            4. return max/k
        '''
        
        if len(nums) == 0 or len(nums) == 1: return nums[0]/k
        
        curSum = maxSum = sum(nums[:k])
        
        for i in range(k, len(nums)):
            curSum += nums[i] - nums[i-k]
            
            maxSum = max(maxSum, curSum)
            
        return maxSum / k
        