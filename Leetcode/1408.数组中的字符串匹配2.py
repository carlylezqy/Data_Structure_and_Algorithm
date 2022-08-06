#
# @lc app=leetcode.cn id=1408 lang=python3
#
# [1408] 数组中的字符串匹配
#
from typing import List
# @lc code=start
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        als=','.join(words)
        res=[]
        for s in words:
            if als.count(s) != 1:
                res.append(s)
        return res

# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    output = solution.stringMatching(["leetcoder","leetcode","od","hamlet","am"])
    print(output)