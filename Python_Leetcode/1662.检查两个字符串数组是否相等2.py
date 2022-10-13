#
# @lc app=leetcode.cn id=1662 lang=python3
#
# [1662] 检查两个字符串数组是否相等
#
from typing import List
# @lc code=start
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        get_array = lambda x: [i for w in x for i in tuple(w)]
        return get_array(word1) == get_array(word2)
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    output = solution.arrayStringsAreEqual(["a", "cb"], ["ab", "c"])
    print(output)