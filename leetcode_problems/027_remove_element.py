class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        while val in nums:
            nums.remove(val)
        k = len(nums)

        return k


nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2

solution = Solution()
k = solution.removeElement(nums, val)
print(k)


# 11 ms (beats 95.42%)
# 13.22 MB (beats 53.96%)
