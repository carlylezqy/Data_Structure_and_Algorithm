#
# @lc app=leetcode.cn id=2114 lang=python3
#
# [2114] 句子中的最多单词数
#

# @lc code=start
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_val = 0
        for i in sentences:
            max_val = max_val if max_val > len(i.split(' ')) else len(i.split(' '))

        return max_val

# @lc code=end

