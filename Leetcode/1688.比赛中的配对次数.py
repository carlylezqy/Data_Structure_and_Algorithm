#
# @lc app=leetcode.cn id=1688 lang=python3
#
# [1688] 比赛中的配对次数
#

# @lc code=start
class Solution:
    def numberOfMatches(self, n: int) -> int:
        return n-1

# n个队伍，1支获胜队伍，所以淘汰n-1个队伍，
# 每淘汰一个队伍需要进性一次比赛
        
# @lc code=end

