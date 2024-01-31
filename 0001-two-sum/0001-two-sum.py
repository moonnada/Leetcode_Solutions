class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        newMap = defaultdict(int)
        
        for i in range(len(nums)):
            lookFor = target - nums[i]
            if lookFor in newMap:
                return [i, newMap[lookFor] ]
            else:
                newMap[nums[i]] = i
        
        # newMap = {}
        # for i in range(len(nums)):
        #     lookFor = target - nums[i]
        #     if lookFor in newMap:
        #         print(newMap[lookFor])
        #         return [i, newMap[lookFor]]
        #     else:
        #         newMap[nums[i]] = i