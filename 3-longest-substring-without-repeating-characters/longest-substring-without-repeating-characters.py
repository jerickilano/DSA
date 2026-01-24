class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Time: O(n) Space: O(n)
        # Sliding Window
        # left at 0, right iterate
        # Each iteration: add to set and get the max length between left & right
        # Check in each iteration: while right value is seen in set, move left += 1
        if not s:
            return 0

        seen = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            max_len = max(max_len, right - left + 1)
            
        return max_len