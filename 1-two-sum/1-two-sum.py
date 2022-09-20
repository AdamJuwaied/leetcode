class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for x, n in enumerate(nums):
            if target - n in nums and x != nums.index(target - n):
                return x, nums.index(target - n)