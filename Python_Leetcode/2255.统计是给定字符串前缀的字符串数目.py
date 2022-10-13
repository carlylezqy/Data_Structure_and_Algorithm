#
# @lc app=leetcode.cn id=2255 lang=python3
#
# [2255] 统计是给定字符串前缀的字符串数目
#

# @lc code=start
class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        count = [1 for i in range(len(words)) if s.startswith(words[i])]
        return sum(count)
# @lc code=end

