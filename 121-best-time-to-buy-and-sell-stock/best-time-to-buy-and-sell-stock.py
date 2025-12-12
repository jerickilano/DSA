class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Sliding Window
        # Time: O(n) Space: O(1)
        left = 0
        right = 1
        maxP = 0
        while right < len(prices):
            if prices[left] < prices[right]:
                maxP = max(maxP, prices[right] - prices[left])
            else:
                left = right
            right += 1
        return maxP