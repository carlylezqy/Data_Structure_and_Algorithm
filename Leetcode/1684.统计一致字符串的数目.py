#
# @lc app=leetcode.cn id=1684 lang=python3
#
# [1684] 统计一致字符串的数目
#
from typing import List
# @lc code=start
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for i in words:
            if set(i).issubset(set(allowed)):
                count += 1
        return count
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    output = solution.countConsistentStrings(allowed="abc", words=["a","b","c","ab","ac","bc","abc"])
    print(output)