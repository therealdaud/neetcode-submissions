class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sin = set()

        for num in nums:
            sin.add(num)

        max_con = 0
        for s in sin:
            if s - 1 not in sin:
                length = 1
                current = s
                while current + 1 in sin:
                    current += 1
                    length += 1
                max_con = max(max_con,length)
        
    
        return max_con


