class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        ans = []
        
        for i, val in enumerate(nums):
            complement = target - val
            if complement in seen:
                ans.append(seen[complement])
                ans.append(i)
            seen[val] = i
        
        for j in range(len(nums)):
            need = target - nums[j]
            if need in seen and seen[need] != j:
                return [j, seen[need]]










#       seen = {}
#      ans = []
#        for index, num in enumerate(nums):
#            seen[index] = num


#        for i in range(len(nums)):
#            need = target - nums[i]
#            if need in seen:
#                ans.append(seen[need])
            

#        return ans




        
            

