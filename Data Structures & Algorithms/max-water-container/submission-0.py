class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        max_water = 0
        while i < j:
            water = (j - i) * min(heights[i], heights[j])
            max_water = max(max_water, water)
            if heights[i] < heights[j]:
                i += 1
            elif heights[i] > heights[j]:
                j -= 1
            else:
                i += 1
                j -= 1
        return max_water
                
