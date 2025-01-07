'''Given an integer array nums, handle multiple queries of the following type:

Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).'''

class NumArray:
    sum_nums: List[int] = List[int]
    
    def __init__(self, nums: List[int]):
        self.sum_nums = [0] * len(nums)
        
        for i in range(0, len(nums)):
            if i == 0:
                self.sum_nums[i] = nums[i]    
            else: 
                self.sum_nums[i] = self.sum_nums[i-1] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.sum_nums[right]
        return self.sum_nums[right] - self.sum_nums[left - 1]
        
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
