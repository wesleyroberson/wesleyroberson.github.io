class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[int(len(nums) / 2)]


nums = [2, 2, 1, 1, 1, 2, 2]

solution = Solution()
k = solution.majorityElement(nums)
print(k)

# 115 ms (beats 91.05%)
# 15.00 MB (beats 46.71%)
