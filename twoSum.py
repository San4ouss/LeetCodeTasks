class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return list((i, j))
        return None


s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))
print(s.twoSum([3, 2, 4], 6))
print(s.twoSum([3, 3], 6))
print(s.twoSum([2, 5, 5, 11], 10))
