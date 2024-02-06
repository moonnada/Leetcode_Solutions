class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        Input: nums = [-1,0,1,2,-1,-4]
        Output: [[-1,-1,2],[-1,0,1]]
        
         l  m         r
        [-4,-1,-1,0,1,2]
        
        1. sort the input list
        2. traverse the sorted list to find valid triplets
            2.1) while l < r and nums[l] == nums[l-1] continue
            2.2) get the cur three sum
            2.3) if the cur sum > 0, r--
            2.4) elif the cur sum <0, r++
            2.5) else put cur three values into the ans list
                2.6) check duplicate values using a loop on the each side
        '''
        
        nums.sort()
        ans =[]
        for i, val in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]: continue
                
            mid, right = i+1, len(nums)-1
            
            while mid < right:
                curSum = val + nums[mid] + nums[right]
                
                if curSum > 0:
                    right -=1
                elif curSum < 0:
                    mid+=1
                else:
                    ans.append([val, nums[mid], nums[right]])
                    mid+=1
                    
                    while nums[mid] == nums[mid-1] and mid < right:
                        mid += 1
                        
        return ans
        