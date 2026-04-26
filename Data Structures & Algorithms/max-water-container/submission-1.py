class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        
        max_volume = 0

        while l <=r:
            volume_height = min(heights[l], heights[r])
            volume_length = r - l
            total_volume = volume_height * volume_length
            max_volume = max(max_volume, total_volume)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r-= 1
        return max_volume
