class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        repeat = set()

        for num in nums:
            if num not in repeat:
                repeat.add(num)
            else:
                return True
        
        return False

        
    