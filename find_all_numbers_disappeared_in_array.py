'''Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.'''

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        length : int = len(nums)
            seen : list[bool] = [False] * length 
        for num in nums:
            seen[num-1] = True
        return [i+1 for i in range(length) if not seen[i]]
