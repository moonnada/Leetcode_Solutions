class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i,val in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]: continue
                
            mid = i+1
            right = len(nums)-1
            
            while mid < right:
                threeSum = val + nums[mid] + nums[right]
                
                if threeSum > 0: right -= 1
                elif threeSum < 0: mid += 1
                else:
                    ans.append([val, nums[mid], nums[right]])
                    mid += 1
                    
                    while mid < right and nums[mid] == nums[mid-1]: mid += 1
                        
        return ans
        