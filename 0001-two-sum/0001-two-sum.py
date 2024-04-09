class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        newMap = {}
        
        for i in range(len(nums)):
            lookFor = target - nums[i]
            if lookFor in newMap:
                return [i, newMap[lookFor] ]
            else:
                newMap[nums[i]] = i
        