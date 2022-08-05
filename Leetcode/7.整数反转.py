#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        output = int(str(x if x > 0 else str(-x) + "-")[::-1])
        return output
# @lc code=end

