class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Two Pointers used in seperate Strings
        one, two = 0, 0
        res = ""
        while one < len(word1) and two < len(word2):
            res += word1[one]
            res += word2[two]
            one += 1
            two += 1
        
        if one < len(word1):
            while one < len(word1):
                res += word1[one]
                one += 1
        elif two < len(word2):
            while two < len(word2):
                res += word2[two]
                two += 1

        return res