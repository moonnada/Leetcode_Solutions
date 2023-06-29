class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        U:
            key points: always have one repeated num, uses only o(1) space complexity
            
        M: sorting?
        
        P: 
            1. sort input arr
            2. traverse to find a duplicate num
                2.1) if find, return the num
        '''
        # Using Floyd's Tortoise and Hare algorithm
        # to detect the cycle in the linked list
        tortoise = nums[0]
        hare = nums[0]

        # Move tortoise and hare until they meet
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break

        # Reset tortoise to the start of the list
        tortoise = nums[0]

        # Move tortoise and hare at the same speed until they meet again
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]

        # Return the duplicate number
        return tortoise