#
# @lc app=leetcode.cn id=1486 lang=python3
#
# [1486] 数组异或操作
#

# @lc code=start
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        arr = [start + i * 2 for i in range(n)]
        num = 0
        for i in arr:
            num = num ^ i
        return num
# @lc code=end

