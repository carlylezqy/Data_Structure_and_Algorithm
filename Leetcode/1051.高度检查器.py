#
# @lc app=leetcode.cn id=1051 lang=python3
#
# [1051] 高度检查器
#

# @lc code=start
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = sorted(heights)
        return sum(1 for i in range(len(heights)) if heights[i] != sorted_heights[i])
# @lc code=end

