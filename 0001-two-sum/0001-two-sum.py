class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if (j := seen.get(complement)) is not None:
                return [j, i]
            seen[num] = i