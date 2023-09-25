class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max = 0
        diffs = {}
        for i in range(len(prices)):
            for j in range(len(prices)):
                key = str(j) + str(i)
                diffs[key] = prices[j] - prices[i]
        condition = False
        while not condition:
            print(diffs)
            max = max(diffs, key=diffs.get)
            print(max)
            max_index = diffs.get(max)
            if max_index[1] < max_index[0]:
                condition
            else:
                diffs.pop(max)

        return max


prices = [7, 1, 5, 3, 6, 4]

solution = Solution()
k = solution.maxProfit(prices)
print(k)
