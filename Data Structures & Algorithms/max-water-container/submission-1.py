class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        
        most = 0
        while l < r:
            diff = r - l
            high = min(heights[r], heights[l])
            vol = diff * high
            most = max(vol, most)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1


        return most


