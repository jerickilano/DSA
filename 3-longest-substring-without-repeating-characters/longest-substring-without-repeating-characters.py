class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Variable Sliding Window + HashMap
        # if invalid: keep moving left until valid (no repeats)
        seen = {}
        l = 0
        max_count = 0

        for r in range(len(s)):
            seen[s[r]] = seen.get(s[r], 0) + 1
            while seen[s[r]] > 1:
                seen[s[l]] -= 1
                l += 1

            max_count = max(max_count, r - l + 1)
        
        return max_count