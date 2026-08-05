class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        freeze on the first value in nums, then have two pointers with two sum logic to equal a number, if they do, that is a triplet pair, if no pairs do that, then you essentially move on to the next value and freeze it. now when first value is frozen, you start one pointer at right and other pointer at left, but you need a conditional to skip the index which is frozen."""
        nums = sorted(nums)
        triplets = []
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            two_sum = 0 - nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = nums[left] + nums[right]
                    
                if total == two_sum:
                    triplets.append([nums[i],nums[left],nums[right]])
                    right -= 1
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left +=1

                if total > two_sum:
                            right -= 1

                elif total < two_sum:
                            left += 1
                        
                    
        return triplets
                        


                
                