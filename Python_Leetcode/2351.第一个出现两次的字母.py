#
# @lc app=leetcode.cn id=2351 lang=python3
#
# [2351] 第一个出现两次的字母
#

# @lc code=start
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        vis = set()
        for ch in s:
            if ch in vis: return ch
            vis.add(ch)
            
# @lc code=end

