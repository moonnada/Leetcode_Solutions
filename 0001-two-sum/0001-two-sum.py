class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myMap = {}
        for i in range(len(nums)):
            lookFor = target - nums[i]
            if lookFor in myMap:
                return [i, myMap[lookFor]]
            myMap[nums[i]] = i
            
            
#         map (key: idx, val: element)
#   1. traverse the input arr to put key and value
#       1.1) if map has target - cur element, return cur index and map's index
        
    
        