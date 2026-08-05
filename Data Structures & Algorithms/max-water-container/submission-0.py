class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        most = 0
        while left < right:
            diff = right - left
            high = min(heights[right], heights[left])
            vol = diff * high
            most = max(vol, most)
            if heights[left] < heights[right]:
                left += 1
            elif heights[left] >= heights[right]:
                right -= 1


        return most


