#
# @lc app=leetcode.cn id=2220 lang=python3
#
# [2220] 转换数字的最少位翻转次数
#

# @lc code=start
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        return(str(bin(start ^ goal)).count('1'))
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    output = solution.minBitFlips(start=10, goal=7)
    