class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1


haystack = 'leetcode'
needle = 'leeto'

solution = Solution()
k = solution.strStr(haystack, needle)
print(k)

# 7 ms (beats 97.55%)
# 13.40 MB (beats 46.35%)
