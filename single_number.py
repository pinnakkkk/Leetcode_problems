'''Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single_number = nums[0]
        for i in range (1, len(nums)):
            single_number = single_number ^ nums[i]
        return single_number
