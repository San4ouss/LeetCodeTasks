class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in nums:
            while nums.count(i) != 1:
                nums.remove(i)
        return len(nums)

        # return len(sorted(set(nums)))


s = Solution()
print(s.removeDuplicates([1, 1, 2]))
print(s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
print(s.removeDuplicates([1, 1, 1, 1]))
