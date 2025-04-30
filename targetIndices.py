class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)
        res = []
        for i in range(len(nums)):
            if sorted_nums[i] == target:
               res.append(i)
        return res
        
