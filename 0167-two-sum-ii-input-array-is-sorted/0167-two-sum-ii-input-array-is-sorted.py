class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        U:
        q) can arr be empty?
        q) can arr have negative nums?
        ex) [2,7,11,15] t=9
            
        M: two ptrs
        
        P: 
            1. init two ptrs (left and right)
            2. while left< right:
                2.1) if arr[left] + arr[right] < target, then left++
                2.2) elif arr[left] + arr[right] > target, then right--
                2.3) else return [left+1, right+1]
        '''
        
        left, right = 0, len(numbers)-1
        
        while left < right:
            curSum = numbers[left] + numbers[right]
            if curSum < target: left+=1
            elif curSum > target: right-=1
            else: return [left+1, right+1]