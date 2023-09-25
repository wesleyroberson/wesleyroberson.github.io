class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                nums[counter] = nums[i]
                counter += 1

        return counter


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

solution = Solution()
k = solution.removeDuplicates(nums)
print(k)

# 52 ms (beats 93.28%)
# 14.48 MB (beats 72.70%)


# first success:

# for e in nums:
#     while nums.count(e) > 1:
#         nums.remove(e)
# k = len(nums)
#
# return k

# 2486 ms (beats 5.1%)
# 14.4 MB (beats 72.70%)
