class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            lookFor = target - nums[i]
            if lookFor in d:
                return [ i , d[lookFor]]
            
            d[nums[i]] = i
            