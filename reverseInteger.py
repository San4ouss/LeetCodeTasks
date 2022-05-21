class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            if int(str(x)[:0:-1]) * -1 < pow(-2, 31):
                return 0
            return -int(str(x)[:0:-1])
        else:
            if int(str(x)[::-1]) > pow(2, 31) - 1:
                return 0
            return int(str(x)[::-1])


s = Solution()
print(s.reverse(123))
print(s.reverse(-123))
print(s.reverse(120))
print(s.reverse(1534236469))
