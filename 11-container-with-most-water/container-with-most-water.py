class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Two Pointer approach Converging
        # length = 0
        # height = 0
        # max_area = 0
        # [1,8,6,2,5,4,8,3,7]
        #  L
        #                  R
        l, r = 0, len(height) - 1
        max_area = 0
        while l < r:
            width = r - l
            heights = min(height[l], height[r])
            area = width * heights
            #print(width, heights, area)

            max_area = max(max_area, area)

            # shrink based on certain conditions
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return max_area
            
