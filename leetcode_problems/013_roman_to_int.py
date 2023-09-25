class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        for i in range(len(s)):
            if i + 1 < len(s) and romans[s[i]] < romans[s[i + 1]]:
                num -= romans[s[i]]
            else:
                num += romans[s[i]]
        return num


s = 'MMMCMLXXXIX'

solution = Solution()
k = solution.romanToInt(s)
print(k)

# 19 ms (beats 97.39%)
# 13.31 MB (beats 42.36%)
