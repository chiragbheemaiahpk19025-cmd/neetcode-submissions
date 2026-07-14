class Solution:
    def trap(self, heights: List[int]) -> int:
        left_max = [-1]
        right_max = [-1]
        max_water = 0

        for i in range(len(heights)):
            if heights[i] < left_max[-1]:
                left_max.append(left_max[-1])
            else:
                left_max.append(heights[i])

        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > right_max[-1]:
                right_max.append(heights[i])
            else:
                right_max.append(right_max[-1])
        right_max.reverse()

        left_max = left_max[1:]
        right_max = right_max[:-1]
        print(left_max)
        print(right_max)

        i = 0
        while i < len(heights):
            water = min(left_max[i], right_max[i]) - heights[i]
            max_water += water
            i += 1
        return max_water
