class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_array = sorted(nums)
        counted_nums = {}
        for i, num in enumerate(sorted_array):
            if num not in counted_nums:
                counted_nums[num] = i
        result = [counted_nums[num] for num in nums]
        return result
