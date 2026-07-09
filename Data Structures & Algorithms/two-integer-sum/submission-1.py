class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}                       # value -> index
        for i, val in enumerate(nums):
            complement = target - val
            if complement in seen:      # partner already walked past?
                return [seen[complement], i]
            seen[val] = i               # otherwise, remember myself