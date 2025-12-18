class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Variable Sliding Window
        # use a map to map character : freq
        # max_freq = max()
        # iterate through string, add/increment char -> freq, 
        # check if max_freq + k >= window size, then decrement left value and move left

        count = {}
        res = 0
        l = 0
        maxf = 0
        
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res