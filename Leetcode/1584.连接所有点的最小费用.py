#
# @lc app=leetcode.cn id=1584 lang=python3
#
# [1584] 连接所有点的最小费用
#

# @lc code=start
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        for i in points:
            for j in points:
                return(abs(i[0] - j[0]) + abs(i[1] - j[1]))
        
# @lc code=end

