#
# @lc app=leetcode.cn id=1408 lang=python3
#
# [1408] 数组中的字符串匹配
#
from typing import List
# @lc code=start
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        opt = []
        for idx, i in enumerate(words):
            for j in words[idx+1:]:
                if(i != j and (i in j or j in i)):
                    if (i not in opt) and len(i) < len(j):
                        opt.append(i)

                    if (j not in opt) and len(i) >= len(j):
                        opt.append(j)

        return opt

# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    output = solution.stringMatching(["leetcoder","leetcode","od","hamlet","am"])
    print(output)