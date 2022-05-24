class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        sort_strs = sorted(strs, key=len)
        shorten_word = sorted(strs, key=len)[0]
        for i in range(1, len(sort_strs)):
            for j in range(len(shorten_word)):
                if shorten_word[j] != sort_strs[i][j]:
                    shorten_word = shorten_word[:j]
                    break

        return shorten_word


s = Solution()
print(s.longestCommonPrefix(["flower", "flow", "flight"]))
print(s.longestCommonPrefix(["dog", "racecar", "car"]))
