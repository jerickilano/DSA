class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # Sliding Window + HashMap
        # [0,1,2,2]
        #  L
        #  R
        count = defaultdict(int)
        l, total, res = 0, 0, 0

        for r in range(len(fruits)):
            count[fruits[r]] += 1 # default dict makes kay automatically
            total += 1

            while len(count) > 2: # more than 2 unique fruits
                f = fruits[l]
                count[f] -= 1
                total -= 1
                l += 1

                if not count[f]: # if key has value = 0
                    count.pop(f)

            res = max(res, total)

        return res